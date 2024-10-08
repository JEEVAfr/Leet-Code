class Solution {
    public int mySqrt(int x) {

              if(x==1)
            return 1;

        long low = 0, high = x / 2;

        while (low <= high) {

            long mid = low+(high-low)/2;

            if ((mid * mid) == x)
                return (int)mid;

            else if ((mid * mid) < x)
                low = mid + 1;

            else if ((mid * mid) > x)
                high = mid - 1;
        }
        return (int)high;
    
    }
    
    }