im = imread('result_image.jpg');
noOfColors = 2;
s_img = size(im);
r = im(:,:,1);
g = im(:,:,2);
b = im(:,:,3);
disp('K-Means');
inputImg = zeros((s_img(1) * s_img(2)), 3);
inputImg(:,1) = r(:);
inputImg(:,2) = g(:);
inputImg(:,3) = b(:);
inputImg = double(inputImg);
disp('K-Means Processing Started');

function[centroid, pointsInCluster, assignment]= myKmeans(data, nbCluster)
% usage
% function[centroid, pointsInCluster, assignment]=
% myKmeans(data, nbCluster)
%
% Output:
% centroid: matrix in each row are the Coordinates of a centroid
% pointsInCluster: row vector with the nbDatapoints belonging to
% the centroid
% assignment: row Vector with clusterAssignment of the dataRows
%
% Input:
% data in rows
% nbCluster : nb of centroids to determine
%
% (c) by Christian Herta ( www.christianherta.de )
% Modified by Nghia Ho to improve speed

data_dim = length(data(1,:));
nbData   = length(data(:,1));

% init the centroids randomly
data_min = min(data);
data_max = max(data);
data_diff = data_max .- data_min ;

% every row is a centroid
centroid = rand(nbCluster, data_dim);
centroid = centroid .* repmat(data_diff, nbCluster, 1) + repmat(data_min, nbCluster, 1);

% no stopping at start
pos_diff = 1.;

% main loop until

while pos_diff > 0.0
  % E-Step
  assignment = [];

  % assign each datapoint to the closest centroid

  if(nbCluster == 1) % special case
	assignment = ones(size(data,1), 1);
  else
	  dists = [];
	  for c = 1: nbCluster
		d = data - repmat(centroid(c,:), size(data,1), 1);
		d = d .* d;
		d = sum(d, 2); % sum the row values

		dists = [dists d];
	  end

	  [a, assignment] = min(dists');

	  assignment = assignment';
  end

  % for the stoppingCriterion
  oldPositions = centroid;

  % M-Step
  % recalculate the positions of the centroids
  centroid = zeros(nbCluster, data_dim);
  pointsInCluster = zeros(nbCluster, 1);

  for c = 1: nbCluster
	indexes = find(assignment == c);
	d = data(indexes,:);
	centroid(c,:) = sum(d,1);
	pointsInCluster(c,1) = size(d,1);

    if( pointsInCluster(c, 1) != 0)
      centroid( c , : ) = centroid( c, : ) / pointsInCluster(c, 1);
    else
      % set cluster randomly to new position
      centroid( c , : ) = (rand( 1, data_dim) .* data_diff) + data_min;
    end
  end

  %stoppingCriterion
  pos_diff = sum (sum( (centroid .- oldPositions).^2 ) );
end
end
myKmeans(inputImg,5);
#[idx, C] = kmeans(inputImg, noOfColors, 'EmptyAction', 'singleton');
#disp('K-Means Processing Completed');
#palette = round(C);

#imshow(palette)