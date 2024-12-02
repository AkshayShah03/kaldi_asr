import org.vosk.LibVosk;
import org.vosk.Model;
import org.vosk.Recognizer;
import javax.sound.sampled.*;
import java.io.IOException;

public class RealTimeASR {

    public static void main(String[] args) {
        // Set log level
        // If LogLevel is not defined, skip this line or use a placeholder
        // LibVosk.setLogLevel(LogLevel.LOG_INFO);

        String modelPath = "/home/akshay/Downloads/asr/serb_cnn_v1_model_LM2000/serb_cnn_model_LM2000";

        try {
            Model model = new Model(modelPath);

            AudioFormat format = new AudioFormat(16000, 16, 1, true, false);
            DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);
            TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
            line.open(format);
            line.start();

            byte[] buffer = new byte[4096];
            Recognizer recognizer = new Recognizer(model, 16000);

            System.out.println("Start speaking...");

            while (true) {
                int bytesRead = line.read(buffer, 0, buffer.length);
                if (bytesRead > 0) {
                    if (recognizer.acceptWaveForm(buffer, bytesRead)) {
                        System.out.println(recognizer.getResult());
                    } 
                }
            }

        } catch (LineUnavailableException | IOException e) {
            e.printStackTrace();
        }
    }
}





















