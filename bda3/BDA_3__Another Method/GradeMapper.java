import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;

public class GradeMapper extends MapReduceBase
implements Mapper<LongWritable, Text, Text, IntWritable>
{
    public void map(LongWritable key,
                    Text value,
                    OutputCollector<Text, IntWritable> output,
                    Reporter reporter) throws IOException
    {
        String line = value.toString();

        String parts[] = line.split(",");

        String student = parts[0];

        int marks = Integer.parseInt(parts[1]);

        output.collect(new Text(student),
                       new IntWritable(marks));
    }
}
