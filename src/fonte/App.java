package fonte;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;

public class App {
    private static ArrayList<String> fragmentos;
    private static ArrayList<String> palavras;
    private static ArrayList<String> resultado;

    public static void main(String[] args) throws Exception{
        fragmentos = new ArrayList<>();
        palavras = new ArrayList<>();
        resultado = new ArrayList<>();

        leEntrada();

        for (String s : palavras)
            if (procuraMatches(s))
                resultado.add(s);

        escreveSaida();
    }

    private static void escreveSaida() throws Exception{
        BufferedWriter bw = new BufferedWriter(new FileWriter("arquivos/saida"));

        for (String s: resultado)
            bw.write(s + "\n");

        bw.flush();
        bw.close();

    }

    private static void leEntrada() throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("arquivos/fragmentos"));

        for (String line = br.readLine(); line != null; line = br.readLine())
            if (!fragmentos.contains(line.toLowerCase()))
                fragmentos.add(line.toLowerCase());


        BufferedReader br2 = new BufferedReader(new FileReader("arquivos/muitas_palavras"));

        for (String line = br2.readLine(); line != null; line = br2.readLine())
            palavras.add(line.toLowerCase());

        br.close();
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
