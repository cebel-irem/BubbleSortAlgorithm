def bubbleSort(arr):
    n = len(arr) #dizinin eleman sayısını alıp bir değişkene atıyoruz
    
    #Her iterasyonda dizinin sonuna en büyük elemanı yerleşmeli
    for i in range(n):
        #Yer değiştirme olduğunu anlamak için bir değişken ile kontrol ediyoruz. Bir nevi bayrak.
        swapped = False
        
        
        #dizinin içindeki sıralamayı kontrol edip düzenleyeceğiz
        for j in range(0, n-i-1):
            
            #Elemanları karşılaştırıp yer değiştirme işlemi yapacağız.
            #Küçük olan yani j elemanı j+1 olan elemandan küçük olmalı değilse yerlerini değiştir.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                #Bayrağı True yaptık. Yer değiştirme işlemi olduğunu belirttik.
                swapped = True
                
            
        #Hiç değişiklik olmadıysa dizi sıralıdır. Döngüyü bitirebiliriz bu durumda.
        if (swapped == False):
            break
        
        
#Dizi oluşturup test ediyoruz :) 
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
