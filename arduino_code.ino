#include <Servo.h>

Servo ServoA, ServoB, ServoC;

int x=0;
int d=10;
int i;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  ServoA.attach(8);
  ServoB.attach(12);
  ServoC.attach(2);
  ServoA.write(30);
  ServoB.write(30);
  ServoC.write(120);
}

void loop() {

    while (!Serial.available());
  x = Serial.readString().toInt();



if (x>30&&x<130)
{  
ServoA.write(x);
ServoB.write(x);
}

//share
if (x==200)
{ 

  for (i=120;i>=30;i--)
{
ServoC.write(i);
delay(d);
}

  for (i=30;i<=130;i++)
{
ServoA.write(i);
ServoB.write(i);
delay(d);
}


delay(3000);


  for (i=130;i>=30;i--)
{
ServoA.write(i);
ServoB.write(i);
delay(d);
}

  for (i=30;i<=120;i++)
{
ServoC.write(i);
delay(d);
}






}

//edit
if (x==300)
{ 

  for (i=30;i<=130;i++)
{
ServoA.write(i);
ServoB.write(i);
delay(d);
}


delay(7000);


  for (i=130;i>=30;i--)
{
ServoA.write(i);
ServoB.write(i);
delay(d);
}


}





//delete
if (x==400)
{ 
  
  for (i=120;i<=180;i++)
{
ServoC.write(i);
delay(d);
}

  for (i=30;i<=90;i++)
{
ServoA.write(i);
delay(d);
}


  for (i=30;i<=115;i++)
{
ServoB.write(i);
delay(d);
}


delay(10000);



  for (i=115;i>=30;i--)
{
ServoB.write(i);
delay(d);
}


  for (i=90;i>=30;i--)
{
ServoA.write(i);
delay(d);
}


  for (i=180;i>=120;i--)
{
ServoC.write(i);
delay(d);
}



}


}
