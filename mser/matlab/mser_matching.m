file1 = 'E:\OwnWork\Leaf\TestImage\leafs\leafpgm\leaf2.jpg';
file2 = 'E:\OwnWork\Leaf\TestImage\leafs\leafpgm\leaf3.jpg';

I1 = imread(file1);
I2 = imread(file2);

I1 = rgb2gray(I1);
I2 = rgb2gray(I2);

% %Find the SURF features.
% points1 = detectSURFFeatures(I1);
% points2 = detectSURFFeatures(I2);

points1 = detectMSERFeatures(I1);
points2 = detectMSERFeatures(I2);

%Extract the features.
[f1, vpts1] = extractFeatures(I1, points1);
[f2, vpts2] = extractFeatures(I2, points2);

%Retrieve the locations of matched points. The SURF featurevectors are already normalized.
indexPairs = matchFeatures(f1, f2, 'Prenormalized', true) ;
matched_pts1 = vpts1(indexPairs(:, 1));
matched_pts2 = vpts2(indexPairs(:, 2));


figure; showMatchedFeatures(I1,I2,matched_pts1,matched_pts2,'montage');
legend('matched points 1','matched points 2');