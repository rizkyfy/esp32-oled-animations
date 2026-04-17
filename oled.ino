#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "frames.h" 

#define SCREEN_WIDTH 128 
#define SCREEN_HEIGHT 64 
#define I2C_SDA 8
#define I2C_SCL 9
#define OLED_RESET -1
#define SCREEN_ADDRESS 0x3C

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Wire.begin(I2C_SDA, I2C_SCL);
  Wire.setClock(400000); 

  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    for(;;); 
  }
  
  display.clearDisplay();
}

void loop() {
  for (int i = 0; i < totalFrames; i++) {
    display.clearDisplay();
    display.drawBitmap(0, 0, (const unsigned char*)pgm_read_ptr(&(frames[i])), 128, 64, WHITE);
    
    display.display();
    delay(10); 
  }
}