import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import java.util.Hashtable;

public class InsecureResourceInit {

    public static void main(String[] args) {
        try {
            // セキュリティ制約なしに初期化（脆弱）
            Hashtable<String, String> env = new Hashtable<>();
            env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.fscontext.RefFSContextFactory");
            env.put(Context.PROVIDER_URL, "file:/tmp"); // 任意ファイルアクセスが可能

            // JNDI コンテキストの作成（ここが CWE-1204 のポイント）
            Context ctx = new InitialContext(env);

            // 危険なリソース登録（例えばDataSourceなど）
            ctx.bind("jdbc/myDatasource", new Object());

            System.out.println("リソースが初期化されました（脆弱な状態）。");

        } catch (NamingException e) {
            e.printStackTrace();
        }
    }
}
