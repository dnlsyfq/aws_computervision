# Capture image & rectangles
while(True):
    frame = capture.read()...
    image = capture.resize(frame,0.15,...)

    # Detect faces in image , only 100 pixels to detect 
    faces = rekognition.detect_faces(Image={'Bytes':image},...)

    # Draw Rectangles
    for face in faces['FaceDetails']:
        is_smiling = face['Smile']['Value']
        draw_rectangle(image,face['BoundingBox'],is_smiling)

# find face in collection

while(True):

    # detect faces in image
    faces = rekognition.search_faces_by_image(
        CollectionId='...',Image={'Bytes':image},...
    )

    # show name and confidence
    for matches in faces['FaceMatches']:

        if 'ExternalImageId' in matches['Face'].keys():
            name = matches['Face']['ExternalImageId']
            confidence = matches['Face']['Confidence']
        
            cv2.putText(...)



