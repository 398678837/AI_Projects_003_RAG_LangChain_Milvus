import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        print("ViewController viewDidLoad")
        setupUI()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        print("ViewController viewWillAppear")
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        print("ViewController viewDidAppear")
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        print("ViewController viewWillDisappear")
    }

    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        print("ViewController viewDidDisappear")
    }

    private func setupUI() {
        view.backgroundColor = .white

        let titleLabel = UILabel()
        titleLabel.text = "核心组件示例"
        titleLabel.font = .systemFont(ofSize: 24, weight: .bold)
        titleLabel.textAlignment = .center
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(titleLabel)

        let pushButton = UIButton(type: .system)
        pushButton.setTitle("跳转到详情页", for: .normal)
        pushButton.titleLabel?.font = .systemFont(ofSize: 18)
        pushButton.addTarget(self, action: #selector(pushDetail), for: .touchUpInside)
        pushButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(pushButton)

        let presentButton = UIButton(type: .system)
        presentButton.setTitle("模态弹出", for: .normal)
        presentButton.titleLabel?.font = .systemFont(ofSize: 18)
        presentButton.addTarget(self, action: #selector(presentModal), for: .touchUpInside)
        presentButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(presentButton)

        let sendDataButton = UIButton(type: .system)
        sendDataButton.setTitle("传递数据", for: .normal)
        sendDataButton.titleLabel?.font = .systemFont(ofSize: 18)
        sendDataButton.addTarget(self, action: #selector(sendData), for: .touchUpInside)
        sendDataButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(sendDataButton)

        NSLayoutConstraint.activate([
            titleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 40),
            titleLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),

            pushButton.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 40),
            pushButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),

            presentButton.topAnchor.constraint(equalTo: pushButton.bottomAnchor, constant: 30),
            presentButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),

            sendDataButton.topAnchor.constraint(equalTo: presentButton.bottomAnchor, constant: 30),
            sendDataButton.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }

    @objc private func pushDetail() {
        let detailVC = DetailViewController()
        detailVC.title = "详情页"
        navigationController?.pushViewController(detailVC, animated: true)
    }

    @objc private func presentModal() {
        let modalVC = ModalViewController()
        modalVC.modalPresentationStyle = .pageSheet
        present(modalVC, animated: true)
    }

    @objc private func sendData() {
        let dataVC = DataViewController()
        dataVC.message = "Hello from ViewController!"
        dataVC.completion = { [weak self] data in
            print("收到返回数据: \(data)")
            let alert = UIAlertController(title: "收到数据", message: data, preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "确定", style: .default))
            self?.present(alert, animated: true)
        }
        navigationController?.pushViewController(dataVC, animated: true)
    }
}

class DetailViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground

        let label = UILabel()
        label.text = "这是详情页"
        label.font = .systemFont(ofSize: 24)
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)

        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }
}

class ModalViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground

        let label = UILabel()
        label.text = "这是模态页面"
        label.font = .systemFont(ofSize: 24)
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)

        let closeButton = UIButton(type: .system)
        closeButton.setTitle("关闭", for: .normal)
        closeButton.titleLabel?.font = .systemFont(ofSize: 18)
        closeButton.addTarget(self, action: #selector(close), for: .touchUpInside)
        closeButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(closeButton)

        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            closeButton.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
            closeButton.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20)
        ])
    }

    @objc private func close() {
        dismiss(animated: true)
    }
}

class DataViewController: UIViewController {

    var message: String?
    var completion: ((String) -> Void)?

    private let textField = UITextField()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        setupUI()
    }

    private func setupUI() {
        let receivedLabel = UILabel()
        receivedLabel.text = "收到的消息:"
        receivedLabel.font = .systemFont(ofSize: 16)
        receivedLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(receivedLabel)

        let messageLabel = UILabel()
        messageLabel.text = message
        messageLabel.font = .systemFont(ofSize: 18)
        messageLabel.textColor = .systemBlue
        messageLabel.numberOfLines = 0
        messageLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(messageLabel)

        let sendBackLabel = UILabel()
        sendBackLabel.text = "返回数据:"
        sendBackLabel.font = .systemFont(ofSize: 16)
        sendBackLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(sendBackLabel)

        textField.borderStyle = .roundedRect
        textField.placeholder = "输入要返回的数据"
        textField.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(textField)

        let sendButton = UIButton(type: .system)
        sendButton.setTitle("返回数据", for: .normal)
        sendButton.titleLabel?.font = .systemFont(ofSize: 18)
        sendButton.addTarget(self, action: #selector(sendBack), for: .touchUpInside)
        sendButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(sendButton)

        NSLayoutConstraint.activate([
            receivedLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 40),
            receivedLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),

            messageLabel.topAnchor.constraint(equalTo: receivedLabel.bottomAnchor, constant: 10),
            messageLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            messageLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),

            sendBackLabel.topAnchor.constraint(equalTo: messageLabel.bottomAnchor, constant: 40),
            sendBackLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),

            textField.topAnchor.constraint(equalTo: sendBackLabel.bottomAnchor, constant: 10),
            textField.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            textField.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),

            sendButton.topAnchor.constraint(equalTo: textField.bottomAnchor, constant: 30),
            sendButton.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }

    @objc private func sendBack() {
        if let text = textField.text, !text.isEmpty {
            completion?(text)
            navigationController?.popViewController(animated: true)
        }
    }
}

class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        print("应用启动完成")
        return true
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        print("应用进入前台")
    }

    func applicationWillResignActive(_ application: UIApplication) {
        print("应用即将失去活动状态")
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        print("应用进入后台")
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        print("应用即将进入前台")
    }

    func applicationWillTerminate(_ application: UIApplication) {
        print("应用即将终止")
    }
}
