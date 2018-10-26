import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class App {
    private static ArrayList<String> fragmentos;
    private static ArrayList<String> palavras;

    private static void leArquivos() throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("../../arquivos/fragmentos"));

        for (String line = br.readLine(); line != null; line = br.readLine())
            if (!fragmentos.contains(line.toLowerCase()))
                fragmentos.add(line.toLowerCase());


        BufferedReader br2 = new BufferedReader(new FileReader("../../arquivos/palavras"));

        for (String line = br2.readLine(); line != null; line = br2.readLine())
            palavras.add(line.toLowerCase());

    }

    public static void main(String[] args) throws Exception{
        fragmentos = new ArrayList<>();
        palavras = new ArrayList<>();

        leArquivos();

        for (String s : palavras)
            if (procuraMatches(s))
                System.out.println(s);
    }


    private static boolean procuraMatches(String search) {
        for (String s : fragmentos)
            if (search.length() == 0)
                return true;

            else if (search.length() >= s.length())
                if (search.substring(0, s.length()).equalsIgnoreCase(s))
                    if(procuraMatches(search.substring(s.length())))
                        return true;

        return false;
    }

}
