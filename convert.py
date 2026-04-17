import cv2
import numpy as np

video_path = 'nama video kalian.mp4' 
output_file = 'frames.h'
width = 128
height = 64
fps_target = 30 

cap = cv2.VideoCapture(video_path)
fps_asli = cap.get(cv2.CAP_PROP_FPS)
frame_skip = int(fps_asli / fps_target)

if frame_skip < 1: frame_skip = 1

with open(output_file, 'w') as f:
    f.write("#include <pgmspace.h>\n\n")
    
    frame_count = 0
    saved_frames = 0
    arrays = []

    print("Memulai konversi mode Full Screen (Zoom & Crop)...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        if frame_count % frame_skip == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            h_asli, w_asli = gray.shape
            rasio_lebar = 128.0 / w_asli
            tinggi_baru = int(h_asli * rasio_lebar)
            
            resized = cv2.resize(gray, (128, tinggi_baru))
            y_center = tinggi_baru // 2
            y_start = y_center - (64 // 2)
            y_end = y_start + 64

            kanvas_crop = resized[y_start:y_end, 0:128]
            _, bw_image = cv2.threshold(kanvas_crop, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            
            hex_array = []
            for y in range(height):
                for x_byte in range(width // 8):
                    byte = 0
                    for bit in range(8):
                        x = x_byte * 8 + bit
                        if bw_image[y, x] > 0:
                            byte |= (1 << (7 - bit))
                    hex_array.append(f"0x{byte:02X}")
            
            array_name = f"frame_{saved_frames}"
            arrays.append(array_name)
            f.write(f"const unsigned char {array_name}[] PROGMEM = {{\n")
            f.write(", ".join(hex_array))
            f.write("\n};\n\n")
            
            saved_frames += 1
            if saved_frames % 50 == 0:
                print(f"Berhasil mengonversi {saved_frames} frame...")

        frame_count += 1

    f.write("const unsigned char* const frames[] PROGMEM = {\n")
    f.write(",\n".join(arrays))
    f.write("\n};\n")
    f.write(f"const int totalFrames = {saved_frames};\n")

cap.release()
print(f"\nSelesai! {saved_frames} frame disimpan ke {output_file}.")