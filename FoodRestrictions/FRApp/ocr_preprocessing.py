def preprocess(image):
    image = cv2.imread(image)

    max_res = 1600
    
    if (image.shape[0] > image.shape[1]):
        image = cv2.resize(image, None, fx=max_res/image.shape[0], fy=max_res/image.shape[0], interpolation=cv2.INTER_CUBIC)
    else:
        image = cv2.resize(image, None, fx=max_res/image.shape[1], fy=max_res/image.shape[1], interpolation=cv2.INTER_CUBIC)

    image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15) 

    plt.imshow(image) 
    plt.show()

    # increase contrast
    image = cv2.convertScaleAbs(image, alpha=1.0, beta=0)

    lower_color = np.array([0, 0, 0])
    upper_color = np.array([180, 180, 180])

    def threshold_range(im, lo, hi):
        unused, t1 = cv2.threshold(im, lo, 255, type=cv2.THRESH_BINARY)
        unused, t2 = cv2.threshold(im, hi, 255, type=cv2.THRESH_BINARY_INV)
        return cv2.bitwise_and(t1, t2)

    def threshold_video(blur):
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        h = threshold_range(h, lower_color[0], upper_color[0])
        s = threshold_range(s, lower_color[1], upper_color[1])
        v = threshold_range(v, lower_color[2], upper_color[2])
        combined_mask = cv2.bitwise_and(h, cv2.bitwise_and(s, v))
        return combined_mask

    imgf = threshold_video(image)

    plt.imshow(imgf) 
    plt.show()

    rows,cols = imgf.shape

    for i in range(0, rows):
        for j in range(0, cols):
            k = imgf[i][j]
            if k != 0:
              imgf[i][j] = 255

    imgf = cv2.bitwise_not(imgf)
    plt.imshow(imgf) 
    plt.show()

    #denoise- in progress
    dst = imgf

    #find text contours
    contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # at the moment this isn't really useful- eventually this will be used to search
    # specific regions of an image for etxt rather than the entire image
    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 35 and h < 35:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(dst, (x, y), (x + w, y + h), (255, 0, 255), 2)

    return dst
