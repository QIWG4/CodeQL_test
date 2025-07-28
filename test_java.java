import java.io.*;
import java.util.Scanner;

public class test_java {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=== 電卓ツール（Java）===");
        System.out.println("1. 四則演算");
        System.out.println("2. コマンド実行");
        System.out.println("3. ファイル読み込み");
        System.out.print("選択してください: ");
        String choice = scanner.nextLine();

        if (choice.equals("1")) {
            System.out.print("計算式を入力してください (例: 1+2): ");
            String expr = scanner.nextLine();
            javax.script.ScriptEngineManager mgr = new javax.script.ScriptEngineManager();
            javax.script.ScriptEngine engine = mgr.getEngineByName("JavaScript");
            System.out.println("結果: " + engine.eval(expr));  // CWE-94
        } else if (choice.equals("2")) {
            System.out.print("実行するコマンドを入力してください: ");
            String cmd = scanner.nextLine();
            Process p = Runtime.getRuntime().exec(cmd);  // CWE-78
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } else if (choice.equals("3")) {
            System.out.print("ファイルパスを入力してください: ");
            String filename = scanner.nextLine();
            BufferedReader reader = new BufferedReader(new FileReader(filename));  // CWE-22
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } else {
            System.out.println("無効な選択です。");
        }

        scanner.close();
    }
}
