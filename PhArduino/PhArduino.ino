#define PH_PIN A0 // ph input
 
float calibration_value = 15.00 ; // adjust the calibration value based on the pH of distilled water
int phval = 0; // set the initial ph value as 0
unsigned long int avgval; 
int buffer_arr[100],temp; // define an array for later data smoothing
int delaytime = 1100; // Set the delay to 10 seconds
 
void setup()
{
  Serial.begin(9600); // the serial monitor setting
}
void loop()
{
  //Over the course of a little under 10 seconds, take 100 sample analog values and store them in an array to smooth the output value.
 for(int i=0;i<100;i++) 
 { 
 buffer_arr[i]=analogRead(PH_PIN);
 delay(10);
 }
 
 //sort the Analog values received in ascending order, because we need to calculate the running average of samples later
 for(int i=0;i<99;i++)
 {
 for(int j=i+1;j<100;j++)
  {
 if(buffer_arr[i]>buffer_arr[j])
    {
 temp=buffer_arr[i];
 buffer_arr[i]=buffer_arr[j];
 buffer_arr[j]=temp;
    }
  }
 }
 //calculate the average of sample Analog values
 avgval=0;
 for(int i=40;i<60;i++)
 avgval+=buffer_arr[i];
 
 //converted the average analog value into actual pH value
 float volt=(float)avgval*5.0/1023/20;
 float ph_act = -5.70 * volt + calibration_value;
 
 // print the pH value in serial monitor:
 Serial.println(ph_act);
 //Serial.print(ph_act);
 //Serial.println((String)"Voltage: "+volt);
 //Serial.print(volt);
 delay(delaytime); // read the pH value every 10 seconds
}