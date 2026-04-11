import UIKit

class ViewController: UIViewController {

    private var data: [String] = ["苹果", "香蕉", "橙子", "葡萄", "西瓜", "草莓", "蓝莓", "芒果", "菠萝", "猕猴桃"]
    private let tableView = UITableView()
    private let animatedView = UIView()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        setupUI()
    }

    private func setupUI() {
        let scrollView = UIScrollView()
        scrollView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(scrollView)

        let contentView = UIView()
        contentView.translatesAutoresizingMaskIntoConstraints = false
        scrollView.addSubview(contentView)

        let titleLabel = UILabel()
        titleLabel.text = "UI开发示例"
        titleLabel.font = .systemFont(ofSize: 24, weight: .bold)
        titleLabel.textAlignment = .center
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(titleLabel)

        let usernameField = UITextField()
        usernameField.placeholder = "用户名"
        usernameField.borderStyle = .roundedRect
        usernameField.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(usernameField)

        let passwordField = UITextField()
        passwordField.placeholder = "密码"
        passwordField.borderStyle = .roundedRect
        passwordField.isSecureTextEntry = true
        passwordField.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(passwordField)

        let loginButton = UIButton(type: .system)
        loginButton.setTitle("登录", for: .normal)
        loginButton.backgroundColor = .systemBlue
        loginButton.setTitleColor(.white, for: .normal)
        loginButton.layer.cornerRadius = 8
        loginButton.addTarget(self, action: #selector(login), for: .touchUpInside)
        loginButton.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(loginButton)

        let switchLabel = UILabel()
        switchLabel.text = "记住密码:"
        switchLabel.font = .systemFont(ofSize: 16)
        switchLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(switchLabel)

        let rememberSwitch = UISwitch()
        rememberSwitch.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(rememberSwitch)

        let sliderLabel = UILabel()
        sliderLabel.text = "音量:"
        sliderLabel.font = .systemFont(ofSize: 16)
        sliderLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(sliderLabel)

        let slider = UISlider()
        slider.minimumValue = 0
        slider.maximumValue = 100
        slider.value = 50
        slider.addTarget(self, action: #selector(sliderChanged(_:)), for: .valueChanged)
        slider.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(slider)

        let sliderValueLabel = UILabel()
        sliderValueLabel.text = "50"
        sliderValueLabel.tag = 100
        sliderValueLabel.font = .systemFont(ofSize: 16)
        sliderValueLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(sliderValueLabel)

        let segmentedLabel = UILabel()
        segmentedLabel.text = "选择:"
        segmentedLabel.font = .systemFont(ofSize: 16)
        segmentedLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(segmentedLabel)

        let segmentedControl = UISegmentedControl(items: ["选项1", "选项2", "选项3"])
        segmentedControl.selectedSegmentIndex = 0
        segmentedControl.addTarget(self, action: #selector(segmentChanged(_:)), for: .valueChanged)
        segmentedControl.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(segmentedControl)

        let animateButton = UIButton(type: .system)
        animateButton.setTitle("播放动画", for: .normal)
        animateButton.addTarget(self, action: #selector(animate), for: .touchUpInside)
        animateButton.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(animateButton)

        animatedView.backgroundColor = .systemRed
        animatedView.layer.cornerRadius = 25
        animatedView.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(animatedView)

        let tableLabel = UILabel()
        tableLabel.text = "列表:"
        tableLabel.font = .systemFont(ofSize: 16)
        tableLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(tableLabel)

        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
        tableView.dataSource = self
        tableView.delegate = self
        tableView.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(tableView)

        NSLayoutConstraint.activate([
            scrollView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            scrollView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            scrollView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            scrollView.bottomAnchor.constraint(equalTo: view.bottomAnchor),

            contentView.topAnchor.constraint(equalTo: scrollView.topAnchor),
            contentView.leadingAnchor.constraint(equalTo: scrollView.leadingAnchor),
            contentView.trailingAnchor.constraint(equalTo: scrollView.trailingAnchor),
            contentView.bottomAnchor.constraint(equalTo: scrollView.bottomAnchor),
            contentView.widthAnchor.constraint(equalTo: scrollView.widthAnchor),

            titleLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 20),
            titleLabel.centerXAnchor.constraint(equalTo: contentView.centerXAnchor),

            usernameField.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 30),
            usernameField.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 30),
            usernameField.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -30),
            usernameField.heightAnchor.constraint(equalToConstant: 44),

            passwordField.topAnchor.constraint(equalTo: usernameField.bottomAnchor, constant: 15),
            passwordField.leadingAnchor.constraint(equalTo: usernameField.leadingAnchor),
            passwordField.trailingAnchor.constraint(equalTo: usernameField.trailingAnchor),
            passwordField.heightAnchor.constraint(equalToConstant: 44),

            loginButton.topAnchor.constraint(equalTo: passwordField.bottomAnchor, constant: 20),
            loginButton.leadingAnchor.constraint(equalTo: usernameField.leadingAnchor),
            loginButton.trailingAnchor.constraint(equalTo: usernameField.trailingAnchor),
            loginButton.heightAnchor.constraint(equalToConstant: 44),

            switchLabel.topAnchor.constraint(equalTo: loginButton.bottomAnchor, constant: 20),
            switchLabel.leadingAnchor.constraint(equalTo: usernameField.leadingAnchor),

            rememberSwitch.centerYAnchor.constraint(equalTo: switchLabel.centerYAnchor),
            rememberSwitch.trailingAnchor.constraint(equalTo: usernameField.trailingAnchor),

            sliderLabel.topAnchor.constraint(equalTo: switchLabel.bottomAnchor, constant: 20),
            sliderLabel.leadingAnchor.constraint(equalTo: usernameField.leadingAnchor),

            slider.centerYAnchor.constraint(equalTo: sliderLabel.centerYAnchor),
            slider.leadingAnchor.constraint(equalTo: sliderLabel.trailingAnchor, constant: 20),
            slider.trailingAnchor.constraint(equalTo: sliderValueLabel.leadingAnchor, constant: -10),

            sliderValueLabel.centerYAnchor.constraint(equalTo: sliderLabel.centerYAnchor),
            sliderValueLabel.trailingAnchor.constraint(equalTo: usernameField.trailingAnchor),
            sliderValueLabel.widthAnchor.constraint(equalToConstant: 30),

            segmentedLabel.topAnchor.constraint(equalTo: sliderLabel.bottomAnchor, constant: 20),
            segmentedLabel.leadingAnchor.constraint(equalTo: usernameField.leadingAnchor),

            segmentedControl.topAnchor.constraint(equalTo: segmentedLabel.bottomAnchor, constant: 10),
            segmentedControl.leadingAnchor.constraint(equalTo: usernameField.leadingAnchor),
            segmentedControl.trailingAnchor.constraint(equalTo: usernameField.trailingAnchor),

            animateButton.topAnchor.constraint(equalTo: segmentedControl.bottomAnchor, constant: 20),
            animateButton.centerXAnchor.constraint(equalTo: contentView.centerXAnchor),

            animatedView.topAnchor.constraint(equalTo: animateButton.bottomAnchor, constant: 20),
            animatedView.centerXAnchor.constraint(equalTo: contentView.centerXAnchor),
            animatedView.widthAnchor.constraint(equalToConstant: 50),
            animatedView.heightAnchor.constraint(equalToConstant: 50),

            tableLabel.topAnchor.constraint(equalTo: animatedView.bottomAnchor, constant: 30),
            tableLabel.leadingAnchor.constraint(equalTo: usernameField.leadingAnchor),

            tableView.topAnchor.constraint(equalTo: tableLabel.bottomAnchor, constant: 10),
            tableView.leadingAnchor.constraint(equalTo: contentView.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor),
            tableView.heightAnchor.constraint(equalToConstant: 300),
            tableView.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -20)
        ])
    }

    @objc private func login() {
        let alert = UIAlertController(title: "提示", message: "登录按钮被点击", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "确定", style: .default))
        present(alert, animated: true)
    }

    @objc private func sliderChanged(_ sender: UISlider) {
        if let label = view.viewWithTag(100) as? UILabel {
            label.text = "\(Int(sender.value))"
        }
    }

    @objc private func segmentChanged(_ sender: UISegmentedControl) {
        print("选中了第\(sender.selectedSegmentIndex)个选项")
    }

    @objc private func animate() {
        UIView.animate(withDuration: 1.0, delay: 0, options: .curveEaseInOut) {
            self.animatedView.transform = CGAffineTransform(scaleX: 2, y: 2)
            self.animatedView.alpha = 0.5
        } completion: { _ in
            UIView.animate(withDuration: 1.0) {
                self.animatedView.transform = .identity
                self.animatedView.alpha = 1
            }
        }
    }
}

extension ViewController: UITableViewDataSource, UITableViewDelegate {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = data[indexPath.row]
        return cell
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        print("选中了: \(data[indexPath.row])")
    }
}

class CustomView: UIView {
    override func draw(_ rect: CGRect) {
        guard let context = UIGraphicsGetCurrentContext() else { return }
        
        let center = CGPoint(x: rect.midX, y: rect.midY)
        let radius = min(rect.width, rect.height) / 2 - 10
        
        context.setFillColor(UIColor.systemBlue.cgColor)
        context.addArc(center: center, radius: radius, startAngle: 0, endAngle: .pi * 2, clockwise: false)
        context.fill()
    }
}
