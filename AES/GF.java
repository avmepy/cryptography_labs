package AES128;

public class GF {

    int num;
    static int modulo = 0x011b;

    public GF(int decimal){
        this.num = decimal;
    }

    public static GF add(GF a, GF b){
        return new GF(a.num ^ b.num);
    }

    public static GF mul(GF a, GF b){
        int res = 0;
        for (int i = 0; i < 8; ++i){
            if (((1 << i) & b.num) != 0){
                int tmp = a.num;
                for (int j = 0; j < i; ++j){
                    tmp = tmp << 1;
                    if (tmp >= 256){
                        tmp = tmp ^ GF.modulo;
                    }
                }
                res = res ^ tmp;
            }
        }
        return new GF(res);

    }

    public static GF pow(GF a, int b){
        GF val = new GF(1);
        while (b > 0){
            val = GF.mul(val, a);
            b--;
        }
        return val;
    }

    public String toString(){
        String res = Integer.toHexString(this.num);
        if (res.length() == 1){
            res = "0" + res;
        }
        return "0x" + res;
    }
}
