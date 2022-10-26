import java.util.Scanner;

public class Biodata {

    public static void main(String[] args) {
        String name;
        int kelas;
        int nim;

        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan NIM : ");
        nim = input.nextInt();
        System.out.print("Masukan Nama: ");
        name = input.next();
        System.out.print("Masukkan Kelas : ");
        kelas = input.nextInt();
        input.close();

        System.out.println("======= Biodata Anda =========");
        System.out.println("NIM : " + nim);
        System.out.println("Nama : " + name);
        System.out.println("Kelas : " + kelas);
    }
}
