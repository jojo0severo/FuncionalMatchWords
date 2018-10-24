import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Stack;

public class App {
    static ArrayList<String> fragmentos;
    static ArrayList<String> palavras;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader("fragmentos.txt"));
        fragmentos = new ArrayList<>();
        palavras = new ArrayList<>();
//        StringBuilder stringona = new StringBuilder();


        for(String line = br.readLine(); line!= null; line = br.readLine()){
//            stringona.append(line).append("\n");
            fragmentos.add(line.toLowerCase());
        }

        BufferedReader br2 = new BufferedReader(new FileReader("palavras"));

        for (String line = br2.readLine(); line!=null; line = br2.readLine()){
            palavras.add(line.toLowerCase());
        }

        for (String s: palavras) {
            if (percorrePalavras(s)){
                System.out.println("Palavra aceita: " + s);
            }
        }

    }

    static Stack<String> stack = new Stack<>();

    private static boolean percorrePalavras(String search){
        for (String s: fragmentos){
            if (esgotaPalavra(search,s)){
                stack.push(s);
            }
        }
        if (stack.size() > 0) {
            return montaPalavra(search, "");
        }
        else
            return false;

    }

    private static boolean esgotaPalavra(String search, String regex){
        if (search.length() > 2) {
            if (search.substring(0, regex.length()).equals(regex)){
                return true;
            }
            return esgotaPalavra(search.substring(1), regex);
        }
        else
            return search.equals(regex);
    }

    private static boolean montaPalavra(String search, String montada) {
        montada += stack.pop();
        montaPalavra(search, montada);

        return search.equals(montada);

    }
}
