### 相关说明

1. 通过 两个程序对拍 来测试代码
2. parameter.json文件中：
    - testNum: 对拍组数
    - nodeLimit: 生成数据的最大节点数
    - edgeLimit: 生成数据的最大边数
    - jar1: 要进行对拍的jar包的名称
    - jar2: 同上
3. 测评机需要导入 cyaron 库

### 使用步骤：
1. 将 jar1.jar 和 jar2.jar 替换成你要进行对拍的jar包，再将parameter.json文件中 “jar1” 和 “jar2”的值改为你要进行对拍的jar包的名称；
2. 运行 main.py；
3. 运行结果说明：
    - jar1的运行结果保存在自动生成的output1.txt中，jar2保存在output2.txt中；
    - 每组测试数据保存在input.txt中；
    - 对拍结果不一致时可通过上述文件查错。