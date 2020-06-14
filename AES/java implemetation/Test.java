
import java.util.Arrays;

public class Test {

    public static void main(String args[]){
        int[][] plainText = {
                {0x32, 0x88, 0x31, 0xe0},
                {0x43, 0x5a, 0x31, 0x37},
                {0xf6, 0x30, 0x98, 0x07},
                {0xa8, 0x8d, 0xa2, 0x34}
        };

        System.out.println("Plain text:");
        for (int i = 0; i < 4; i++) {
            System.out.println(Arrays.toString(plainText[i]));
        }

        int[][] key = {
                {0x2b, 0x28, 0xab, 0x09},
                {0x7e, 0xae, 0xf7, 0xcf},
                {0x15, 0xd2, 0x15, 0x4f},
                {0x16, 0xa6, 0x88, 0x3c}
        };

        AES aes = new AES(key);
        int[][] cipherText = aes.encrypt(plainText);
        int[][] decodedText = aes.decrypt(cipherText);

        System.out.println("Decoded text:");
        for (int i = 0; i < 4; i++) {
            System.out.println(Arrays.toString(decodedText[i]));
        }

    }
}
