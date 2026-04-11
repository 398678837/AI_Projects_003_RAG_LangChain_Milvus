import Foundation

print("=== Swift 最佳实践示例 ===")

protocol NetworkService {
    func fetchData(from url: URL) async throws -> Data
}

class NetworkManager: NetworkService {
    private let session: URLSession
    
    init(session: URLSession = .shared) {
        self.session = session
    }
    
    func fetchData(from url: URL) async throws -> Data {
        let (data, response) = try await session.data(from: url)
        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.invalidResponse
        }
        return data
    }
}

protocol DataRepository {
    func fetchUsers() async throws -> [User]
    func saveUser(_ user: User) async throws
}

class UserRepository: DataRepository {
    private let networkService: NetworkService
    private let localStore: LocalStore
    
    init(networkService: NetworkService = NetworkManager(),
         localStore: LocalStore = UserDefaultsStore()) {
        self.networkService = networkService
        self.localStore = localStore
    }
    
    func fetchUsers() async throws -> [User] {
        if let cachedUsers = try? await localStore.fetchUsers() {
            return cachedUsers
        }
        
        guard let url = URL(string: "https://api.example.com/users") else {
            throw NetworkError.invalidURL
        }
        
        let data = try await networkService.fetchData(from: url)
        let users = try JSONDecoder().decode([User].self, from: data)
        try await localStore.saveUsers(users)
        return users
    }
    
    func saveUser(_ user: User) async throws {
        try await localStore.saveUser(user)
    }
}

protocol LocalStore {
    func fetchUsers() async throws -> [User]
    func saveUsers(_ users: [User]) async throws
    func saveUser(_ user: User) async throws
}

class UserDefaultsStore: LocalStore {
    private let defaults = UserDefaults.standard
    private let usersKey = "cached_users"
    
    func fetchUsers() async throws -> [User] {
        guard let data = defaults.data(forKey: usersKey) else {
            throw LocalStoreError.noData
        }
        return try JSONDecoder().decode([User].self, from: data)
    }
    
    func saveUsers(_ users: [User]) async throws {
        let data = try JSONEncoder().encode(users)
        defaults.set(data, forKey: usersKey)
    }
    
    func saveUser(_ user: User) async throws {
        var users = (try? await fetchUsers()) ?? []
        if let index = users.firstIndex(where: { $0.id == user.id }) {
            users[index] = user
        } else {
            users.append(user)
        }
        try await saveUsers(users)
    }
}

struct User: Codable, Identifiable {
    let id: UUID
    let name: String
    let email: String
    let createdAt: Date
}

enum NetworkError: Error, LocalizedError {
    case invalidURL
    case invalidResponse
    case requestFailed(statusCode: Int)
    case decodingError(Error)
    
    var errorDescription: String? {
        switch self {
        case .invalidURL: return "无效的URL"
        case .invalidResponse: return "无效的响应"
        case .requestFailed(let code): return "请求失败，状态码: \(code)"
        case .decodingError(let error): return "解码错误: \(error.localizedDescription)"
        }
    }
}

enum LocalStoreError: Error {
    case noData
    case saveFailed
}

class UserViewModel: ObservableObject {
    @Published var users: [User] = []
    @Published var isLoading = false
    @Published var errorMessage: String?
    
    private let repository: DataRepository
    
    init(repository: DataRepository = UserRepository()) {
        self.repository = repository
    }
    
    func loadUsers() async {
        await MainActor.run {
            isLoading = true
            errorMessage = nil
        }
        
        do {
            let users = try await repository.fetchUsers()
            await MainActor.run {
                self.users = users
                self.isLoading = false
            }
        } catch {
            await MainActor.run {
                self.errorMessage = error.localizedDescription
                self.isLoading = false
            }
        }
    }
}

class SafeTimer {
    private weak var target: AnyObject?
    private let action: () -> Void
    private var timer: Timer?
    
    init(target: AnyObject, interval: TimeInterval, action: @escaping () -> Void) {
        self.target = target
        self.action = action
        self.timer = Timer.scheduledTimer(
            timeInterval: interval,
            target: self,
            selector: #selector(fire),
            userInfo: nil,
            repeats: true
        )
    }
    
    @objc private func fire() {
        guard target != nil else {
            timer?.invalidate()
            return
        }
        action()
    }
    
    func invalidate() {
        timer?.invalidate()
        timer = nil
    }
}

class Singleton {
    static let shared = Singleton()
    private init() {}
    
    func doSomething() {
        print("Singleton doing something")
    }
}

struct Configuration {
    static let apiBaseURL = "https://api.example.com"
    static let timeout: TimeInterval = 30
    static let maxRetryCount = 3
}

extension String {
    var trimmed: String {
        return trimmingCharacters(in: .whitespacesAndNewlines)
    }
    
    var isEmail: Bool {
        let emailRegEx = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}"
        let predicate = NSPredicate(format: "SELF MATCHES %@", emailRegEx)
        return predicate.evaluate(with: self)
    }
}

extension Optional where Wrapped == String {
    var orEmpty: String {
        return self ?? ""
    }
}

func performOperation<T>(
    retryCount: Int = Configuration.maxRetryCount,
    operation: () async throws -> T
) async rethrows -> T {
    var lastError: Error?
    for _ in 0..<retryCount {
        do {
            return try await operation()
        } catch {
            lastError = error
            try await Task.sleep(nanoseconds: 1_000_000_000)
        }
    }
    throw lastError!
}

class ViewController {
    private var viewModel: UserViewModel!
    private var cancellables = Set<AnyCancellable>()
    
    func setupBindings() {
        viewModel.$users
            .sink { [weak self] users in
                self?.updateUI(with: users)
            }
            .store(in: &cancellables)
        
        viewModel.$isLoading
            .sink { [weak self] isLoading in
                self?.showLoading(isLoading)
            }
            .store(in: &cancellables)
    }
    
    func updateUI(with users: [User]) {
        print("更新UI，用户数量: \(users.count)")
    }
    
    func showLoading(_ show: Bool) {
        print(show ? "显示加载中..." : "隐藏加载")
    }
}

struct AnyCancellable {
    let cancel: () -> Void
}

extension Set {
    mutating func store(in cancellables: inout Set<AnyCancellable>) {
    }
}

func safeDivide(_ a: Int, by b: Int) -> Result<Int, DivisionError> {
    guard b != 0 else {
        return .failure(.divisionByZero)
    }
    return .success(a / b)
}

enum DivisionError: Error {
    case divisionByZero
}

func exampleUsage() {
    print("\n--- 1. 依赖注入示例 ---")
    
    let networkService = NetworkManager()
    let localStore = UserDefaultsStore()
    let repository = UserRepository(networkService: networkService, localStore: localStore)
    let viewModel = UserViewModel(repository: repository)
    print("ViewModel创建完成")
    
    print("\n--- 2. 字符串扩展示例 ---")
    
    let dirtyString = "  Hello, Swift!  "
    print("原始字符串: '\(dirtyString)'")
    print("修剪后: '\(dirtyString.trimmed)'")
    
    let email = "test@example.com"
    print("\(email) 是邮箱: \(email.isEmail)")
    
    let optionalString: String? = nil
    print("可选字符串: '\(optionalString.orEmpty)'")
    
    print("\n--- 3. 安全操作示例 ---")
    
    let result1 = safeDivide(10, by: 2)
    switch result1 {
    case .success(let value):
        print("10 / 2 = \(value)")
    case .failure(let error):
        print("错误: \(error)")
    }
    
    let result2 = safeDivide(10, by: 0)
    switch result2 {
    case .success(let value):
        print("10 / 0 = \(value)")
    case .failure(let error):
        print("错误: \(error)")
    }
    
    print("\n--- 4. 单例示例 ---")
    Singleton.shared.doSomething()
    
    print("\n--- 5. 常量配置示例 ---")
    print("API Base URL: \(Configuration.apiBaseURL)")
    print("Timeout: \(Configuration.timeout)秒")
    print("Max Retry Count: \(Configuration.maxRetryCount)")
}

exampleUsage()

print("\n=== Swift 最佳实践示例结束 ===")
