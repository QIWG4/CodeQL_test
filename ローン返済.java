import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.text.DecimalFormat;

@WebServlet("/loan")
public class LoanServlet extends HttpServlet {
    private static final DecimalFormat df = new DecimalFormat("#,##0.00");

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        String pStr = req.getParameter("principal");
        String rStr = req.getParameter("rate");
        String yStr = req.getParameter("years");

        resp.setContentType("text/html; charset=UTF-8");
        resp.getWriter().println("<html><body><h2>ローン計算結果</h2>");

        try {
            double principal = Double.parseDouble(pStr);
            double annualRate = Double.parseDouble(rStr);
            int years = Integer.parseInt(yStr);

            double r = annualRate / 12.0 / 100.0;
            int n = years * 12;
            double payment = principal * (r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);

            resp.getWriter().println("<p>入力: Principal=" + pStr
                    + ", Rate=" + rStr + "%, Years=" + yStr + "</p>");
            resp.getWriter().println("<p>月々の返済額: " + df.format(payment) + " 円</p>");
        } catch (Exception e) {
            resp.getWriter().println("<p>入力エラーがあります: " + e.getMessage() + "</p>");
        }

        resp.getWriter().println("</body></html>");
    }
}
