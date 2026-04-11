import Foundation

print("=== 数据存储示例 ===")

class UserDefaultsManager {
    static let shared = UserDefaultsManager()
    private let defaults = UserDefaults.standard
    
    private enum Keys {
        static let username = "username"
        static let isDarkMode = "isDarkMode"
        static let fontSize = "fontSize"
        static let favoriteColors = "favoriteColors"
        static let userProfile = "userProfile"
    }
    
    var username: String? {
        get { defaults.string(forKey: Keys.username) }
        set { defaults.set(newValue, forKey: Keys.username) }
    }
    
    var isDarkMode: Bool {
        get { defaults.bool(forKey: Keys.isDarkMode) }
        set { defaults.set(newValue, forKey: Keys.isDarkMode) }
    }
    
    var fontSize: Double {
        get { defaults.double(forKey: Keys.fontSize) }
        set { defaults.set(newValue, forKey: Keys.fontSize) }
    }
    
    var favoriteColors: [String] {
        get { defaults.stringArray(forKey: Keys.favoriteColors) ?? [] }
        set { defaults.set(newValue, forKey: Keys.favoriteColors) }
    }
    
    func saveUserProfile(_ profile: UserProfile) {
        if let data = try? JSONEncoder().encode(profile) {
            defaults.set(data, forKey: Keys.userProfile)
        }
    }
    
    func loadUserProfile() -> UserProfile? {
        guard let data = defaults.data(forKey: Keys.userProfile) else {
            return nil
        }
        return try? JSONDecoder().decode(UserProfile.self, from: data)
    }
    
    func clearAll() {
        defaults.removeObject(forKey: Keys.username)
        defaults.removeObject(forKey: Keys.isDarkMode)
        defaults.removeObject(forKey: Keys.fontSize)
        defaults.removeObject(forKey: Keys.favoriteColors)
        defaults.removeObject(forKey: Keys.userProfile)
        defaults.synchronize()
    }
}

struct UserProfile: Codable {
    let name: String
    let email: String
    let age: Int
    let preferences: [String: Bool]
}

class FileManagerHelper {
    static let shared = FileManagerHelper()
    private let fileManager = FileManager.default
    
    var documentsDirectory: URL {
        return fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
    }
    
    var cachesDirectory: URL {
        return fileManager.urls(for: .cachesDirectory, in: .userDomainMask).first!
    }
    
    var applicationSupportDirectory: URL {
        let url = fileManager.urls(for: .applicationSupportDirectory, in: .userDomainMask).first!
        try? fileManager.createDirectory(at: url, withIntermediateDirectories: true)
        return url
    }
    
    func fileURL(in directory: DirectoryType, fileName: String) -> URL {
        let baseURL: URL
        switch directory {
        case .documents: baseURL = documentsDirectory
        case .caches: baseURL = cachesDirectory
        case .applicationSupport: baseURL = applicationSupportDirectory
        }
        return baseURL.appendingPathComponent(fileName)
    }
    
    func saveString(_ string: String, to url: URL) throws {
        try string.write(to: url, atomically: true, encoding: .utf8)
    }
    
    func loadString(from url: URL) throws -> String {
        return try String(contentsOf: url, encoding: .utf8)
    }
    
    func saveData(_ data: Data, to url: URL) throws {
        try data.write(to: url, options: .atomic)
    }
    
    func loadData(from url: URL) throws -> Data {
        return try Data(contentsOf: url)
    }
    
    func saveArray<T: Codable>(_ array: [T], to url: URL) throws {
        let data = try JSONEncoder().encode(array)
        try saveData(data, to: url)
    }
    
    func loadArray<T: Codable>(from url: URL) throws -> [T] {
        let data = try loadData(from: url)
        return try JSONDecoder().decode([T].self, from: data)
    }
    
    func fileExists(at url: URL) -> Bool {
        return fileManager.fileExists(atPath: url.path)
    }
    
    func deleteFile(at url: URL) throws {
        try fileManager.removeItem(at: url)
    }
    
    func listFiles(in directory: URL) throws -> [URL] {
        return try fileManager.contentsOfDirectory(at: directory, includingPropertiesForKeys: nil)
    }
    
    enum DirectoryType {
        case documents, caches, applicationSupport
    }
}

class PlistManager {
    static let shared = PlistManager()
    
    func savePlist<T: Encodable>(_ value: T, to url: URL) throws {
        let encoder = PropertyListEncoder()
        encoder.outputFormat = .xml
        let data = try encoder.encode(value)
        try data.write(to: url)
    }
    
    func loadPlist<T: Decodable>(from url: URL, type: T.Type) throws -> T {
        let data = try Data(contentsOf: url)
        let decoder = PropertyListDecoder()
        return try decoder.decode(type, from: data)
    }
    
    func saveDictionary(_ dict: [String: Any], to url: URL) {
        (dict as NSDictionary).write(to: url, atomically: true)
    }
    
    func loadDictionary(from url: URL) -> [String: Any]? {
        return NSDictionary(contentsOf: url) as? [String: Any]
    }
}

struct AppSettings: Codable {
    var notificationsEnabled: Bool
    var soundEnabled: Bool
    var autoSave: Bool
    var lastUpdated: Date
}

class SimpleKeychainHelper {
    static let shared = SimpleKeychainHelper()
    
    private let service = "com.example.myapp"
    
    func savePassword(_ password: String, account: String) -> Bool {
        guard let data = password.data(using: .utf8) else { return false }
        
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
            kSecValueData as String: data
        ]
        
        SecItemDelete(query as CFDictionary)
        
        let status = SecItemAdd(query as CFDictionary, nil)
        return status == errSecSuccess
    }
    
    func getPassword(account: String) -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
            kSecReturnData as String: kCFBooleanTrue!,
            kSecMatchLimit as String: kSecMatchLimitOne
        ]
        
        var data: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &data)
        
        guard status == errSecSuccess,
              let passwordData = data as? Data,
              let password = String(data: passwordData, encoding: .utf8) else {
            return nil
        }
        
        return password
    }
    
    func deletePassword(account: String) -> Bool {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account
        ]
        
        let status = SecItemDelete(query as CFDictionary)
        return status == errSecSuccess
    }
}

func exampleUsage() {
    print("\n--- 1. UserDefaults示例 ---")
    
    let userDefaults = UserDefaultsManager.shared
    userDefaults.username = "张三"
    userDefaults.isDarkMode = true
    userDefaults.fontSize = 16.0
    userDefaults.favoriteColors = ["红色", "蓝色", "绿色"]
    
    let profile = UserProfile(
        name: "张三",
        email: "zhangsan@example.com",
        age: 25,
        preferences: ["notifications": true, "darkMode": true]
    )
    userDefaults.saveUserProfile(profile)
    
    print("用户名: \(userDefaults.username ?? "无")")
    print("深色模式: \(userDefaults.isDarkMode)")
    print("字体大小: \(userDefaults.fontSize)")
    print("喜欢的颜色: \(userDefaults.favoriteColors)")
    if let loadedProfile = userDefaults.loadUserProfile() {
        print("用户资料: \(loadedProfile.name), \(loadedProfile.email)")
    }
    
    print("\n--- 2. 文件存储示例 ---")
    
    let fileHelper = FileManagerHelper.shared
    let testFile = fileHelper.fileURL(in: .documents, fileName: "test.txt")
    
    try? fileHelper.saveString("Hello, 文件存储!", to: testFile)
    if let content = try? fileHelper.loadString(from: testFile) {
        print("文件内容: \(content)")
    }
    
    let numbers = [1, 2, 3, 4, 5]
    let numbersFile = fileHelper.fileURL(in: .documents, fileName: "numbers.json")
    try? fileHelper.saveArray(numbers, to: numbersFile)
    if let loadedNumbers: [Int] = try? fileHelper.loadArray(from: numbersFile) {
        print("数组: \(loadedNumbers)")
    }
    
    print("\n--- 3. Property List示例 ---")
    
    let plistManager = PlistManager.shared
    let settingsFile = fileHelper.fileURL(in: .documents, fileName: "settings.plist")
    
    var settings = AppSettings(
        notificationsEnabled: true,
        soundEnabled: false,
        autoSave: true,
        lastUpdated: Date()
    )
    
    try? plistManager.savePlist(settings, to: settingsFile)
    if let loadedSettings = try? plistManager.loadPlist(from: settingsFile, type: AppSettings.self) {
        print("设置 - 通知: \(loadedSettings.notificationsEnabled), 声音: \(loadedSettings.soundEnabled)")
    }
    
    let dict: [String: Any] = [
        "name": "李四",
        "age": 30,
        "hobbies": ["读书", "游泳", "编程"]
    ]
    let dictFile = fileHelper.fileURL(in: .documents, fileName: "data.plist")
    plistManager.saveDictionary(dict, to: dictFile)
    if let loadedDict = plistManager.loadDictionary(from: dictFile) {
        print("字典: \(loadedDict)")
    }
    
    print("\n--- 4. 简单Keychain示例 ---")
    
    let keychain = SimpleKeychainHelper.shared
    let account = "user@example.com"
    let password = "MySecretPassword123"
    
    if keychain.savePassword(password, account: account) {
        print("密码已保存到Keychain")
    }
    
    if let retrievedPassword = keychain.getPassword(account: account) {
        print("从Keychain获取密码: \(retrievedPassword)")
    }
    
    if keychain.deletePassword(account: account) {
        print("密码已从Keychain删除")
    }
}

exampleUsage()

print("\n=== 数据存储示例结束 ===")
