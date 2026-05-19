## 1. 个人信息
- 姓名： 王喆永 
- 院系： 无穹书院
- 学号： 2025012612

## 2. 实现效果
TODO：请附带一个清华云盘的公共链接，指向两个视频，分别以`task1_<学号>`和`task2_<学号>`命名。
1. 对于task1，请参照我们提供的Demo视频，录制你完成的ArUco渲染视频。
2. 对于打靶任务，你需要开启 simulator 后，使用固定 seed=144259 运行一次客户端并录屏，
```bash
uv run python simulator/runner.py --seed 144259
```
请将你录屏时使用的命令和终端输出粘贴在此区域。
```bash
chmod +x simulator/Linux/AutoAim.x86_64
./simulator/Linux/AutoAim.x86_64
[UnityMemory] Configuration Parameters - Can be set up in boot.config
    "memorysetup-bucket-allocator-granularity=16"
    "memorysetup-bucket-allocator-bucket-count=8"
    "memorysetup-bucket-allocator-block-size=4194304"
    "memorysetup-bucket-allocator-block-count=1"
    "memorysetup-main-allocator-block-size=16777216"
    "memorysetup-thread-allocator-block-size=16777216"
    "memorysetup-gfx-main-allocator-block-size=16777216"
    "memorysetup-gfx-thread-allocator-block-size=16777216"
    "memorysetup-cache-allocator-block-size=4194304"
    "memorysetup-typetree-allocator-block-size=2097152"
    "memorysetup-profiler-bucket-allocator-granularity=16"
    "memorysetup-profiler-bucket-allocator-bucket-count=8"
    "memorysetup-profiler-bucket-allocator-block-size=4194304"
    "memorysetup-profiler-bucket-allocator-block-count=1"
    "memorysetup-profiler-allocator-block-size=16777216"
    "memorysetup-profiler-editor-allocator-block-size=1048576"
    "memorysetup-temp-allocator-size-main=4194304"
    "memorysetup-job-temp-allocator-block-size=2097152"
    "memorysetup-job-temp-allocator-block-size-background=1048576"
    "memorysetup-job-temp-allocator-reduction-small-platforms=262144"
    "memorysetup-allocator-temp-initial-block-size-main=262144"
    "memorysetup-allocator-temp-initial-block-size-worker=262144"
    "memorysetup-temp-allocator-size-background-worker=32768"
    "memorysetup-temp-allocator-size-job-worker=262144"
    "memorysetup-temp-allocator-size-preload-manager=262144"
    "memorysetup-temp-allocator-size-nav-mesh-worker=65536"
    "memorysetup-temp-allocator-size-audio-worker=65536"
    "memorysetup-temp-allocator-size-cloud-worker=32768"
    "memorysetup-temp-allocator-size-gfx=262144"
```
```bash
    python -u simulator/runner.py --seed 144259
Game configured: latency=0.5 s, board=1.0x1.0 m
Game ended. Final score: 140.0, accuracy: 0.5652173757553101, precision: 0.30439046025276184
```

https://cloud.tsinghua.edu.cn/d/a6a6abb9b2f74564a46b/
## 3. 改动点
TODO：如果你实现了和现有伪代码或架构不同的点，请在这里说明，并指向具体代码文件的某一行或某一函数，比如：
- 不同的滤波逻辑
- `pipeline.py`中不同的滤波参数（如果想精益求精，调参感觉都得做，因为我们默认的参数很激进）
- `target_selector.py`中不同的选板逻辑

## 4. 遇到的问题与反馈
TODO：可以讲讲你在调参或者探索新的实现过程中遇到的困难和心得，以及你觉得我们可以改进的地方。
小白不是很懂，很多东西都是靠ai完成的，虽然自己能看懂，但是写不出来（捂脸）