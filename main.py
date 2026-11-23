import argparse,csv,json
from collections import Counter
from PIL import Image

def main():
    p=argparse.ArgumentParser();p.add_argument("mask");p.add_argument("classes");p.add_argument("output");a=p.parse_args()
    image=Image.open(a.mask)
    if image.mode not in ("L","I","I;16"): raise ValueError("Mask must contain integer class IDs")
    counts=Counter(image.getdata());names=json.load(open(a.classes,encoding="utf-8"));total=image.width*image.height
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["class_id","class_name","pixels","percent"]);w.writeheader()
        for key,count in sorted(counts.items()):
            w.writerow({"class_id":key,"class_name":names.get(str(key),"unknown"),
                        "pixels":count,"percent":round(100*count/total,3)})
if __name__=="__main__":main()

