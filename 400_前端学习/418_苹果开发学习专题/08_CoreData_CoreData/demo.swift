import CoreData
import SwiftUI

class CoreDataManager {
    static let shared = CoreDataManager()
    
    let container: NSPersistentContainer
    
    var context: NSManagedObjectContext {
        return container.viewContext
    }
    
    private init() {
        container = NSPersistentContainer(name: "DataModel")
        container.loadPersistentStores { description, error in
            if let error = error {
                fatalError("Core Data加载失败: \(error)")
            }
        }
    }
    
    func save() {
        if context.hasChanges {
            do {
                try context.save()
            } catch {
                print("保存失败: \(error)")
            }
        }
    }
    
    func delete(_ object: NSManagedObject) {
        context.delete(object)
        save()
    }
}

extension CoreDataManager {
    func createPerson(name: String, age: Int16, email: String) -> Person {
        let person = Person(context: context)
        person.id = UUID()
        person.name = name
        person.age = age
        person.email = email
        person.createdAt = Date()
        save()
        return person
    }
    
    func fetchAllPersons() -> [Person] {
        let request: NSFetchRequest<Person> = Person.fetchRequest()
        let sortDescriptor = NSSortDescriptor(key: "createdAt", ascending: false)
        request.sortDescriptors = [sortDescriptor]
        
        do {
            return try context.fetch(request)
        } catch {
            print("查询失败: \(error)")
            return []
        }
    }
    
    func fetchPerson(byName name: String) -> [Person] {
        let request: NSFetchRequest<Person> = Person.fetchRequest()
        request.predicate = NSPredicate(format: "name CONTAINS %@", name)
        
        do {
            return try context.fetch(request)
        } catch {
            print("查询失败: \(error)")
            return []
        }
    }
    
    func updatePerson(_ person: Person, name: String? = nil, age: Int16? = nil, email: String? = nil) {
        if let name = name {
            person.name = name
        }
        if let age = age {
            person.age = age
        }
        if let email = email {
            person.email = email
        }
        save()
    }
    
    func deletePerson(_ person: Person) {
        delete(person)
    }
}

class Person: NSManagedObject {
    @NSManaged var id: UUID?
    @NSManaged var name: String?
    @NSManaged var age: Int16
    @NSManaged var email: String?
    @NSManaged var createdAt: Date?
    @NSManaged var tasks: NSSet?
}

extension Person {
    @nonobjc public class func fetchRequest() -> NSFetchRequest<Person> {
        return NSFetchRequest<Person>(entityName: "Person")
    }
}

class Task: NSManagedObject {
    @NSManaged var id: UUID?
    @NSManaged var title: String?
    @NSManaged var completed: Bool
    @NSManaged var dueDate: Date?
    @NSManaged var priority: Int16
    @NSManaged var person: Person?
}

extension Task {
    @nonobjc public class func fetchRequest() -> NSFetchRequest<Task> {
        return NSFetchRequest<Task>(entityName: "Task")
    }
}

struct CoreDataDemoView: View {
    @Environment(\.managedObjectContext) private var viewContext
    
    @FetchRequest(
        sortDescriptors: [NSSortDescriptor(key: "createdAt", ascending: false)],
        animation: .default)
    private var persons: FetchedResults<Person>
    
    @State private var name = ""
    @State private var age = ""
    @State private var email = ""
    
    var body: some View {
        NavigationStack {
            VStack {
                Form {
                    Section("添加人员") {
                        TextField("姓名", text: $name)
                        TextField("年龄", text: $age)
                            .keyboardType(.numberPad)
                        TextField("邮箱", text: $email)
                            .keyboardType(.emailAddress)
                        
                        Button("添加") {
                            addPerson()
                        }
                        .disabled(name.isEmpty || age.isEmpty)
                    }
                }
                .frame(height: 200)
                
                List {
                    ForEach(persons) { person in
                        VStack(alignment: .leading, spacing: 5) {
                            Text(person.name ?? "未知")
                                .font(.headline)
                            Text("年龄: \(person.age)")
                                .font(.subheadline)
                            Text(person.email ?? "")
                                .font(.caption)
                                .foregroundColor(.secondary)
                        }
                    }
                    .onDelete(perform: deletePersons)
                }
            }
            .navigationTitle("CoreData 示例")
        }
    }
    
    private func addPerson() {
        withAnimation {
            let newPerson = Person(context: viewContext)
            newPerson.id = UUID()
            newPerson.name = name
            newPerson.age = Int16(age) ?? 0
            newPerson.email = email
            newPerson.createdAt = Date()
            
            saveContext()
            name = ""
            age = ""
            email = ""
        }
    }
    
    private func deletePersons(offsets: IndexSet) {
        withAnimation {
            offsets.map { persons[$0] }.forEach(viewContext.delete)
            saveContext()
        }
    }
    
    private func saveContext() {
        do {
            try viewContext.save()
        } catch {
            let nsError = error as NSError
            fatalError("Unresolved error \(nsError), \(nsError.userInfo)")
        }
    }
}

class CoreDataViewModel: ObservableObject {
    private let context = CoreDataManager.shared.context
    @Published var persons: [Person] = []
    @Published var errorMessage: String?
    
    func loadPersons() {
        persons = CoreDataManager.shared.fetchAllPersons()
    }
    
    func addPerson(name: String, age: Int16, email: String) {
        _ = CoreDataManager.shared.createPerson(name: name, age: age, email: email)
        loadPersons()
    }
    
    func searchPersons(name: String) {
        persons = CoreDataManager.shared.fetchPerson(byName: name)
    }
    
    func deletePerson(_ person: Person) {
        CoreDataManager.shared.deletePerson(person)
        loadPersons()
    }
}

func coreDataUsageExample() {
    print("=== CoreData 使用示例 ===")
    
    let manager = CoreDataManager.shared
    
    let person1 = manager.createPerson(name: "张三", age: 25, email: "zhangsan@example.com")
    let person2 = manager.createPerson(name: "李四", age: 30, email: "lisi@example.com")
    print("创建了人员: \(person1.name ?? ""), \(person2.name ?? "")")
    
    let allPersons = manager.fetchAllPersons()
    print("所有人员: \(allPersons.map { $0.name ?? "" })")
    
    let searchResults = manager.fetchPerson(byName: "张")
    print("搜索结果: \(searchResults.map { $0.name ?? "" })")
    
    manager.updatePerson(person1, name: "张三丰", age: 26)
    print("更新后: \(person1.name ?? "")")
    
    manager.deletePerson(person2)
    let remaining = manager.fetchAllPersons()
    print("删除后剩余: \(remaining.map { $0.name ?? "" })")
    
    print("=== CoreData 示例结束 ===")
}
