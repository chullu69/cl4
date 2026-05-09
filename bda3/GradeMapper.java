import java.io.IOException;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class GradeMapper extends Mapper<Object, Text, Text, DoubleWritable> {
    private Text studentId = new Text();
    private DoubleWritable score = new DoubleWritable();

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        // Expected input format: student_id,score   (e.g., "S1,85")
        String line = value.toString().trim();
        if (line.isEmpty()) return;
        String[] fields = line.split(",");
        if (fields.length >= 2) {
            studentId.set(fields[0].trim());
            try {
                score.set(Double.parseDouble(fields[1].trim()));
                context.write(studentId, score);
            } catch (NumberFormatException e) {
                // skip bad records
            }
        }
    }
}