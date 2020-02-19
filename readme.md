## 一. 阅读代码重点
**主要代码为transform, segmentation, filter, feature_detection, edges**

###  transform
* swirl 漩涡
* ssim 一个相似度评价
* ransac 匹配算法
* plot_register_rotation 坐标系变换: <span style="color:red">极坐标</span>,
* FFT
* Radon变换 <span style="color:red">重点</span>
* 金字塔
* 仿射
* 立体匹配 
* 边缘扩展
### 分割
* watershed
* 阔值: 比CV多了OTsu
* plot_segmentations: felzenszwalb SLIC quickshift
* regionprops_table  regionprops
* random_walker 随机漫步
* RAG
* peak_local_max
* threshold_niblack  threshold_sauvola <span style="color:red">重点</span>
* graph.cut_normalized
* morphological_chan_vese
* join_segmentations 把多个SEG 合并 <span style="color:red">重点</span>
* floodfill 水漫
* chan_vese
* Extrema 极值

##### floodfill
输入： 选定点，设置高低阈值
输出： 满足阈值的点组成的联通区域
算法： 寻找相邻（4或8连通）区域进行扩散，直到没有新的点可加入。

##### watershed
输入：marker，人工标记一些点（可以是一片区域），对希望区分出来的不同区域的点，赋以不同的值。
输出：算法根据marker的值，计算原图中每个点的归属。
算法：以标记图中的相应标记作为种子点，对梯度图像进行变换，当不同标记汇合时产生分水线。

##### grabcut
输入：选定前景区域或mask点，选取背景mask点
输出：分割后的前景mask点
算法：源于这样的假设，未标记的前景(背景)和标记的前景(背景)有相似的分布，区域是平滑和连通的。

### filter 过滤的做用是去噪,放大,修复等.
* window FFT
* unsharp_mask
* tophat 高帽
* Wiener (restoration)
* Mean filter (rank mean)
* Phase Unwrapping
* Non-local means
* Inpainting 图像修复
* Hysteresis thresholding 滞后阈值法
* Entropy 熵 <span style="color:red">重点</span>
* 小波
* Deconvolution 反卷积
* Shift-invariant wavelet denoising

### feature detection 特征值
* blob 
* brief 需要harries做为角点检测, 才能做brief
* CENSURE <span style="color:red">重点</span>
* Corner 角点 harris
* Dense DAISY feature <span style="color:red">重点</span> 分块统计梯度方向直方图，不同的是，DAISY在分块策略上进行了改进，利用高斯卷积来进行梯度方向直方图的分块汇聚，这样利用高斯卷积的可快速计算性就可以快速稠密地进行特征描述子的提取
* Gabor filter 
* grey level co-occurrence matrix  灰度共生矩阵  是一种典型的统计分析方法
* Haar-like feature 
* HOG
* Local Binary Pattern  分类
* ORB feature
* Shape
* template Correlation 相关计算
* Sliding window histogram  滑动窗口直方图 这个好像也是用互相关计算的. 

### edge
* canny
* convex_hull
* hough
* Skeletonize 骨架化 用的还是形态学
* shapes 建立各种规则图形
* Scharr Edge Detection / Scharr - Prewitt / Scharr - Sobel <span style="color:red">重点</span>
* Contour
