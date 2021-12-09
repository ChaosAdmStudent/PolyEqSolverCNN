import cv2
import numpy as np

def Image_read(image):
    x = cv2.imread(image)
    x = cv2.cvtColor(x,cv2.COLOR_BGR2RGB)
    return x
    
def segment_image(img):
    eqImg = [img]

    eqlist=[] #equation list

    #another data for no padding in the end
    eqnopadlist=[]
    for images in eqImg:
        image = Image_read(images)
        pixel_values = image.reshape((-1, 3))
        # convert to float
        pixel_values = np.float32(pixel_values)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        k = 2
        _, labels, (centers) = cv2.kmeans(pixel_values, k, None,criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        centers2=np.uint8([[255,255,255],[0,0,0]])
        # flatten the labels array
        labels = labels.flatten()
        segmented_image = centers2[labels.flatten()]
        segmented_image = segmented_image.reshape(image.shape)
        # show the image
        if(segmented_image[0,0,0]!=0):
            segmented_image=~segmented_image
        img=segmented_image
        flag=0
        #only R from RGB
        first=0
        last=0
        imglist=[]
        flag2=0
        firstfr=0
        #1269 since i+10 in loop
        for i in range(img.shape[1]-6):
            if np.sum(img[:,i,0])==0 :
                if np.sum(img[:,firstfr+6,0])==0 :
                    flag2=0
                if np.sum(img[:,firstfr+6,0])!=0 :
                    if flag==1:
                        if np.sum(img[:,i+4,0])==0:
                            last=i
                            #cut here on right on middle +5
                            imglist.append(img[:,first:last+2,:])
                            first=i+2
                            flag2=0
                            flag=0

                    continue
            if np.sum(img[:,i,0])!=0:
                if flag2==0:
                    firstfr=i
                flag2=1
                flag=1
                continue
        for m in range(len(imglist)):       
            var0=np.var(imglist[m][:,:,0],axis=0)
            var1=np.var(imglist[m][:,:,0],axis=1)
            middle=len(var1)
            indices0=[i for i in list(range(len(var0))) if var0[i]==0]
            indices1=[i for i in list(range(len(var1)-5)) if var1[i]==0 and np.sum(var1[i+5])==0]
            temp0=imglist[m]
            temp0=np.delete(temp0,indices0,axis=1)
            temp0=np.delete(temp0,indices1,axis=0)
            eqnopadlist.append(temp0)
            temp0=np.pad(temp0[:,:,0],pad_width=10,mode='constant',constant_values=0)
            temp0=np.repeat(temp0[:,:,np.newaxis],3,axis=2)
        
            eqlist.append(temp0)
    
    return eqnopadlist 

def get_eqlabels(): 
    eq_test=[4,13,3,11,8,12,3,13,2,10,9,13]
    return eq_test

def resize(eqlist): 
    dsize = (64, 64) 
    eqtemp=eqlist 
    for i in range(len(eqtemp)):
        eqtemp[i] = cv2.resize(eqlist[i], dsize) 
    
    return eqtemp 

if __name__ == '__main__': 
    PATH = r'C:\\Users\\lakshya\\Documents\\VIT\\5th Semester\\ML\\Flask\\dataset'
    eqImg=sorted(glob.glob(f"{PATH}\\eqfinal\\*"))
    print(eqImg)
    print('--------')
    eqImg = segment_image(eqImg) 
    print(eqImg)
    print('--------')
    eqLabels = get_eqlabels() 
    print('--------')
    eqtemp = resize(eqImg) 
    x_eq2 = np.array(eqtemp) 

    print(eqtemp)
    print(x_eq2.shape)