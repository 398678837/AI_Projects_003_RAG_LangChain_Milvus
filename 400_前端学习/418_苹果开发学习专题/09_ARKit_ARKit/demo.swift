import ARKit
import SceneKit
import UIKit

class ARViewController: UIViewController, ARSCNViewDelegate {

    var sceneView: ARSCNView!
    var coachingOverlayView: ARCoachingOverlayView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupARView()
        setupCoachingOverlay()
        setupTapGesture()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        startARSession()
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        sceneView.session.pause()
    }
    
    func setupARView() {
        sceneView = ARSCNView(frame: view.bounds)
        sceneView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(sceneView)
        
        sceneView.delegate = self
        sceneView.showsStatistics = true
        sceneView.autoenablesDefaultLighting = true
        
        let scene = SCNScene()
        sceneView.scene = scene
    }
    
    func setupCoachingOverlay() {
        coachingOverlayView = ARCoachingOverlayView(frame: view.bounds)
        coachingOverlayView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        coachingOverlayView.session = sceneView.session
        coachingOverlayView.goal = .horizontalPlane
        coachingOverlayView.activatesAutomatically = true
        view.addSubview(coachingOverlayView)
    }
    
    func setupTapGesture() {
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(handleTap(_:)))
        sceneView.addGestureRecognizer(tapGesture)
    }
    
    func startARSession() {
        let configuration = ARWorldTrackingConfiguration()
        configuration.planeDetection = [.horizontal, .vertical]
        configuration.environmentTexturing = .automatic
        sceneView.session.run(configuration)
    }
    
    @objc func handleTap(_ gesture: UITapGestureRecognizer) {
        let location = gesture.location(in: sceneView)
        
        let hitTestResults = sceneView.hitTest(location, types: .existingPlaneUsingExtent)
        
        if let hitTestResult = hitTestResults.first {
            addBox(at: hitTestResult)
        } else if let hitTestResult = sceneView.raycastQuery(from: location, allowing: .estimatedPlane, alignment: .any) {
            let results = sceneView.session.raycast(hitTestResult)
            if let result = results.first {
                addBox(at: result)
            }
        }
    }
    
    func addBox(at hitTestResult: ARHitTestResult) {
        let box = SCNBox(width: 0.1, height: 0.1, length: 0.1, chamferRadius: 0.01)
        
        let material = SCNMaterial()
        material.diffuse.contents = UIColor.systemBlue
        box.materials = [material]
        
        let node = SCNNode(geometry: box)
        node.position = SCNVector3(
            hitTestResult.worldTransform.columns.3.x,
            hitTestResult.worldTransform.columns.3.y + Float(box.height / 2),
            hitTestResult.worldTransform.columns.3.z
        )
        
        sceneView.scene.rootNode.addChildNode(node)
        
        addRotationAnimation(to: node)
    }
    
    func addBox(at raycastResult: ARRaycastResult) {
        let box = SCNBox(width: 0.1, height: 0.1, length: 0.1, chamferRadius: 0.01)
        
        let material = SCNMaterial()
        material.diffuse.contents = UIColor.systemRed
        box.materials = [material]
        
        let node = SCNNode(geometry: box)
        node.simdPosition = raycastResult.worldTransform.translation
        node.position.y += Float(box.height / 2)
        
        sceneView.scene.rootNode.addChildNode(node)
        
        addRotationAnimation(to: node)
    }
    
    func addSphere(at position: SCNVector3) {
        let sphere = SCNSphere(radius: 0.05)
        
        let material = SCNMaterial()
        material.diffuse.contents = UIColor.systemGreen
        sphere.materials = [material]
        
        let node = SCNNode(geometry: sphere)
        node.position = position
        
        sceneView.scene.rootNode.addChildNode(node)
    }
    
    func addRotationAnimation(to node: SCNNode) {
        let rotation = SCNAction.rotateBy(x: 0, y: .pi * 2, z: 0, duration: 5)
        let repeatRotation = SCNAction.repeatForever(rotation)
        node.runAction(repeatRotation)
    }
    
    func renderer(_ renderer: SCNSceneRenderer, didAdd node: SCNNode, for anchor: ARAnchor) {
        if let planeAnchor = anchor as? ARPlaneAnchor {
            addPlaneVisualization(to: node, with: planeAnchor)
        }
    }
    
    func renderer(_ renderer: SCNSceneRenderer, didUpdate node: SCNNode, for anchor: ARAnchor) {
        if let planeAnchor = anchor as? ARPlaneAnchor {
            updatePlaneVisualization(node, with: planeAnchor)
        }
    }
    
    func addPlaneVisualization(to node: SCNNode, with anchor: ARPlaneAnchor) {
        let plane = SCNPlane(
            width: CGFloat(anchor.extent.x),
            height: CGFloat(anchor.extent.z)
        )
        
        let material = SCNMaterial()
        material.diffuse.contents = anchor.alignment == .horizontal ?
            UIColor.systemBlue.withAlphaComponent(0.3) :
            UIColor.systemYellow.withAlphaComponent(0.3)
        plane.materials = [material]
        
        let planeNode = SCNNode(geometry: plane)
        planeNode.eulerAngles.x = -.pi / 2
        planeNode.position = SCNVector3(anchor.center.x, 0, anchor.center.z)
        
        node.addChildNode(planeNode)
    }
    
    func updatePlaneVisualization(_ node: SCNNode, with anchor: ARPlaneAnchor) {
        guard let planeNode = node.childNodes.first,
              let plane = planeNode.geometry as? SCNPlane else {
            return
        }
        
        plane.width = CGFloat(anchor.extent.x)
        plane.height = CGFloat(anchor.extent.z)
        planeNode.position = SCNVector3(anchor.center.x, 0, anchor.center.z)
    }
    
    func session(_ session: ARSession, didFailWithError error: Error) {
        print("AR会话失败: \(error.localizedDescription)")
    }
    
    func sessionWasInterrupted(_ session: ARSession) {
        print("AR会话被中断")
    }
    
    func sessionInterruptionEnded(_ session: ARSession) {
        print("AR会话中断结束")
        startARSession()
    }
}

class SimpleARView: UIView {
    var arView: ARSCNView!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupARView()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setupARView()
    }
    
    func setupARView() {
        arView = ARSCNView(frame: bounds)
        arView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        addSubview(arView)
    }
    
    func startSession() {
        let config = ARWorldTrackingConfiguration()
        config.planeDetection = .horizontal
        arView.session.run(config)
    }
    
    func addCube() {
        let cube = SCNBox(width: 0.1, height: 0.1, length: 0.1, chamferRadius: 0.01)
        cube.materials.first?.diffuse.contents = UIColor.red
        let node = SCNNode(geometry: cube)
        node.position = SCNVector3(0, 0, -0.5)
        arView.scene.rootNode.addChildNode(node)
    }
}

func printARKitInfo() {
    print("=== ARKit 信息 ===")
    print("ARWorldTrackingConfiguration.isSupported: \(ARWorldTrackingConfiguration.isSupported)")
    print("ARFaceTrackingConfiguration.isSupported: \(ARFaceTrackingConfiguration.isSupported)")
    print("ARBodyTrackingConfiguration.isSupported: \(ARBodyTrackingConfiguration.isSupported)")
    print("=== ARKit 信息结束 ===")
}
