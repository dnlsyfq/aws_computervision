# create a collection & load faces

# create face collection
aws rekognition create-collection --collection-id trainers

# create index collection
aws rekognition index-faces
--collection-id trainers
--image "S3Object={Bucket=hands-on-rekognition,Name=dan.jpg}"
--external-image-id dan


# search for faces

aws rekognition start-face-search
--video "S3Object={Bucket=...,Name=trainers.mp4"
--collection-id trainers

aws rekognition get-face-search --job-id...

