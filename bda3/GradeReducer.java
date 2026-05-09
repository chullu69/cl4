import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class GradeReducer extends Reducer<Text, DoubleWritable, Text, Text> {
    private Text grade = new Text();

    public void reduce(Text key, Iterable<DoubleWritable> values, Context context)
            throws IOException, InterruptedException {
        double total = 0;
        int count = 0;
        for (DoubleWritable val : values) {
            total += val.get();
            count++;
        }
        double average = (count == 0) ? 0 : total / count;
        String gradeStr = calculateGrade(average);
        grade.set(gradeStr);
        context.write(key, grade);
    }

    private String calculateGrade(double avg) {
        if (avg >= 90) return "A";
        else if (avg >= 80) return "B";
        else if (avg >= 70) return "C";
        else if (avg >= 60) return "D";
        else return "F";
    }
}