class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n==0) return true;
        if (n==1 && flowerbed[0]==0 && flowerbed.length==1) return true;
    
        if (flowerbed.length<3){
            if (n>1) return false;
            else {
                if (flowerbed.length==1) return flowerbed[0]==0;
                else return flowerbed[0]==0 && flowerbed[0]==flowerbed[1]; 
            }
        } 
        if (flowerbed[0]==flowerbed[1] && flowerbed[1]==0) {
            flowerbed[0]=1;
            n--;
        }
        for (int i=1; i<flowerbed.length-1; i++){
            if (flowerbed[i-1]==0 && flowerbed[i+1]==0 && flowerbed[i]==0) {
                flowerbed[i]=1;

                n--;
            }
        }
        if (flowerbed[flowerbed.length-1]==flowerbed[flowerbed.length-2] && flowerbed[flowerbed.length-1]==0) n--;
        return n<=0;


        
    }
}
