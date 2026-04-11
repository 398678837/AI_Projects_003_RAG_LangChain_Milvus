import AppKit

class AppDelegate: NSObject, NSApplicationDelegate {

    var window: NSWindow!

    func applicationDidFinishLaunching(_ aNotification: Notification) {
        print("应用启动完成")
        
        window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 800, height: 600),
            styleMask: [.titled, .closable, .miniaturizable, .resizable],
            backing: .buffered,
            defer: false
        )
        window.center()
        window.title = "AppKit示例"
        
        let viewController = MainViewController()
        window.contentViewController = viewController
        
        window.makeKeyAndOrderFront(nil)
    }

    func applicationWillTerminate(_ aNotification: Notification) {
        print("应用即将终止")
    }
}

class MainViewController: NSViewController {

    var count = 0
    var label: NSTextField!
    var button: NSButton!
    var textField: NSTextField!

    override func loadView() {
        view = NSView(frame: NSRect(x: 0, y: 0, width: 800, height: 600))
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        print("视图加载完成")
        setupUI()
    }

    func setupUI() {
        view.wantsLayer = true
        view.layer?.backgroundColor = NSColor.windowBackgroundColor.cgColor

        let titleLabel = NSTextField(labelWithString: "AppKit 示例")
        titleLabel.font = NSFont.systemFont(ofSize: 24, weight: .bold)
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(titleLabel)

        label = NSTextField(labelWithString: "计数: 0")
        label.font = NSFont.systemFont(ofSize: 18)
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)

        button = NSButton(title: "点击我", target: self, action: #selector(buttonClicked))
        button.bezelStyle = .rounded
        button.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(button)

        let inputLabel = NSTextField(labelWithString: "输入:")
        inputLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(inputLabel)

        textField = NSTextField()
        textField.placeholderString = "请输入内容"
        textField.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(textField)

        let displayButton = NSButton(title: "显示输入", target: self, action: #selector(displayInput))
        displayButton.bezelStyle = .rounded
        displayButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(displayButton)

        let resultLabel = NSTextField(labelWithString: "结果将显示在这里")
        resultLabel.tag = 100
        resultLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(resultLabel)

        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            titleLabel.topAnchor.constraint(equalTo: view.topAnchor, constant: 40),

            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 40),

            button.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            button.topAnchor.constraint(equalTo: label.bottomAnchor, constant: 20),

            inputLabel.topAnchor.constraint(equalTo: button.bottomAnchor, constant: 40),
            inputLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 100),

            textField.topAnchor.constraint(equalTo: inputLabel.bottomAnchor, constant: 10),
            textField.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 100),
            textField.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -100),
            textField.heightAnchor.constraint(equalToConstant: 30),

            displayButton.topAnchor.constraint(equalTo: textField.bottomAnchor, constant: 20),
            displayButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),

            resultLabel.topAnchor.constraint(equalTo: displayButton.bottomAnchor, constant: 20),
            resultLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }

    @objc func buttonClicked() {
        count += 1
        label.stringValue = "计数: \(count)"
    }

    @objc func displayInput() {
        let input = textField.stringValue
        if let resultLabel = view.viewWithTag(100) as? NSTextField {
            resultLabel.stringValue = "你输入的是: \(input)"
        }
    }
}

class CustomView: NSView {
    override func draw(_ dirtyRect: NSRect) {
        super.draw(dirtyRect)
        
        guard let context = NSGraphicsContext.current?.cgContext else { return }
        
        let center = CGPoint(x: bounds.midX, y: bounds.midY)
        let radius = min(bounds.width, bounds.height) / 2 - 10
        
        context.setFillColor(NSColor.systemBlue.cgColor)
        context.addArc(center: center, radius: radius, startAngle: 0, endAngle: .pi * 2, clockwise: false)
        context.fill()
    }
}

class WindowController: NSWindowController {
    convenience init() {
        self.init(windowNibName: nil)
    }
    
    override func windowDidLoad() {
        super.windowDidLoad()
        window?.title = "我的窗口"
    }
}

let app = NSApplication.shared
let delegate = AppDelegate()
app.delegate = delegate
app.run()
