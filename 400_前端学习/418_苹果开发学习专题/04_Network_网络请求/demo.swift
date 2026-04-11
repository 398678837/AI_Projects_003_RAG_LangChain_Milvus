import Foundation

print("=== 网络请求示例 ===")

struct User: Codable {
    let login: String
    let id: Int
    let avatarUrl: String?
    let name: String?
    let bio: String?
    
    enum CodingKeys: String, CodingKey {
        case login, id, name, bio
        case avatarUrl = "avatar_url"
    }
}

struct Repository: Codable {
    let id: Int
    let name: String
    let fullName: String
    let description: String?
    let stargazersCount: Int
    
    enum CodingKeys: String, CodingKey {
        case id, name, description
        case fullName = "full_name"
        case stargazersCount = "stargazers_count"
    }
}

class NetworkManager {
    static let shared = NetworkManager()
    private let session: URLSession
    
    private init() {
        let config = URLSessionConfiguration.default
        config.timeoutIntervalForRequest = 30
        session = URLSession(configuration: config)
    }
    
    func fetchUser(username: String) async throws -> User {
        guard let url = URL(string: "https://api.github.com/users/\(username)") else {
            throw NetworkError.invalidURL
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        request.setValue("application/vnd.github.v3+json", forHTTPHeaderField: "Accept")
        
        let (data, response) = try await session.data(for: request)
        
        guard let httpResponse = response as? HTTPURLResponse else {
            throw NetworkError.invalidResponse
        }
        
        guard (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.requestFailed(statusCode: httpResponse.statusCode)
        }
        
        let decoder = JSONDecoder()
        decoder.keyDecodingStrategy = .convertFromSnakeCase
        return try decoder.decode(User.self, from: data)
    }
    
    func fetchRepositories(username: String) async throws -> [Repository] {
        guard let url = URL(string: "https://api.github.com/users/\(username)/repos?sort=stars") else {
            throw NetworkError.invalidURL
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        
        let (data, response) = try await session.data(for: request)
        
        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.invalidResponse
        }
        
        let decoder = JSONDecoder()
        decoder.keyDecodingStrategy = .convertFromSnakeCase
        return try decoder.decode([Repository].self, from: data)
    }
    
    func postData(url: URL, parameters: [String: Any]) async throws -> Data {
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONSerialization.data(withJSONObject: parameters)
        
        let (data, response) = try await session.data(for: request)
        
        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.requestFailed(statusCode: (response as? HTTPURLResponse)?.statusCode ?? -1)
        }
        
        return data
    }
    
    func downloadFile(url: URL, destination: URL) async throws {
        let (tempURL, _) = try await session.download(from: url)
        try FileManager.default.moveItem(at: tempURL, to: destination)
    }
}

enum NetworkError: Error, LocalizedError {
    case invalidURL
    case invalidResponse
    case requestFailed(statusCode: Int)
    case decodingError(Error)
    case noData
    
    var errorDescription: String? {
        switch self {
        case .invalidURL:
            return "无效的URL"
        case .invalidResponse:
            return "无效的响应"
        case .requestFailed(let statusCode):
            return "请求失败，状态码: \(statusCode)"
        case .decodingError(let error):
            return "解码失败: \(error.localizedDescription)"
        case .noData:
            return "没有数据"
        }
    }
}

class GitHubViewModel: ObservableObject {
    @Published var user: User?
    @Published var repositories: [Repository] = []
    @Published var isLoading = false
    @Published var errorMessage: String?
    
    private let networkManager = NetworkManager.shared
    
    func fetchUserData(username: String) async {
        await MainActor.run {
            isLoading = true
            errorMessage = nil
        }
        
        do {
            async let user = networkManager.fetchUser(username: username)
            async let repos = networkManager.fetchRepositories(username: username)
            
            let (fetchedUser, fetchedRepos) = try await (user, repos)
            
            await MainActor.run {
                self.user = fetchedUser
                self.repositories = fetchedRepos
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

func exampleUsage() {
    print("\n--- 1. 使用URLSession进行GET请求 ---")
    
    Task {
        do {
            let user = try await NetworkManager.shared.fetchUser(username: "octocat")
            print("用户: \(user.login)")
            print("ID: \(user.id)")
            print("姓名: \(user.name ?? "未知")")
            print("简介: \(user.bio ?? "无")")
        } catch {
            print("错误: \(error.localizedDescription)")
        }
    }
    
    print("\n--- 2. JSON解析示例 ---")
    
    let jsonString = """
    {
        "login": "testuser",
        "id": 12345,
        "avatar_url": "https://example.com/avatar.jpg",
        "name": "Test User",
        "bio": "A test user"
    }
    """
    
    if let jsonData = jsonString.data(using: .utf8) {
        do {
            let decoder = JSONDecoder()
            decoder.keyDecodingStrategy = .convertFromSnakeCase
            let user = try decoder.decode(User.self, from: jsonData)
            print("解析的用户: \(user.login)")
            print("头像URL: \(user.avatarUrl ?? "无")")
        } catch {
            print("解析错误: \(error)")
        }
    }
    
    print("\n--- 3. 自定义CodingKeys ---")
    
    struct Product: Codable {
        let productId: Int
        let productName: String
        let price: Double
        let inStock: Bool
        
        enum CodingKeys: String, CodingKey {
            case productId = "product_id"
            case productName = "product_name"
            case price
            case inStock = "in_stock"
        }
    }
    
    let productJson = """
    {
        "product_id": 1,
        "product_name": "iPhone",
        "price": 999.99,
        "in_stock": true
    }
    """.data(using: .utf8)!
    
    do {
        let product = try JSONDecoder().decode(Product.self, from: productJson)
        print("产品: \(product.productName), 价格: \(product.price), 库存: \(product.inStock)")
    } catch {
        print("产品解析错误: \(error)")
    }
    
    print("\n--- 4. 日期处理 ---")
    
    struct Event: Codable {
        let title: String
        let date: Date
        
        enum CodingKeys: String, CodingKey {
            case title, date
        }
    }
    
    let eventJson = """
    {
        "title": "Meeting",
        "date": "2024-01-15T10:30:00Z"
    }
    """.data(using: .utf8)!
    
    do {
        let decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .iso8601
        let event = try decoder.decode(Event.self, from: eventJson)
        print("事件: \(event.title), 日期: \(event.date)")
    } catch {
        print("事件解析错误: \(error)")
    }
    
    print("\n--- 5. URLSessionConfiguration ---")
    
    let config = URLSessionConfiguration.default
    config.timeoutIntervalForRequest = 30
    config.timeoutIntervalForResource = 300
    config.httpAdditionalHeaders = [
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    ]
    config.requestCachePolicy = .reloadRevalidatingCacheData
    
    let session = URLSession(configuration: config)
    print("URLSession配置完成")
}

exampleUsage()

print("\n=== 网络请求示例结束 ===")
