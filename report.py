import re

# আপনার মেসেজগুলো এখানে পেস্ট করুন
messages = """
14/02/2024, 6:31 am - Amrin: AZ11325 10p 1
14/02/2024, 12:55 pm - Amrin: AZ11330 10p 1
14/02/2024, 1:03 pm - Amrin: AZ11331 3.5 ml 6
14/02/2024, 1:45 pm - Amrin: AZ11332 10p 1
14/02/2024, 1:58 pm - Amrin: AZ11333 10p 1
14/02/2024, 2:25 pm - Amrin: AZ11335 3p 1
14/02/2024, 3:19 pm - Amrin: AZ11336 p 1
14/02/2024, 3:20 pm - Amrin: AZ11337 10p 1
14/02/2024, 3:49 pm - Amrin: AZ11340 3.5 ml 5
15/02/2024, 9:17 am - Amrin: AZ11346 10p 1 <This message was edited>
15/02/2024, 9:19 am - Amrin: AZ11347 10p 1
15/02/2024, 9:26 am - Amrin: AZ11348 3ml 1
"""

# প্রতিটি মেসেজ প্রসেস করার জন্য একটি ফাংশন
def process_message(message):
    # রেগুলার এক্সপ্রেশন দিয়ে অর্ডার নাম্বার এবং কোয়ান্টিটি বের করা
    match = re.search(r'AZ\d+\s+\d+\w+\s+\d+', message)
    if match:
        # ম্যাচ পাওয়া গেলে সেই অংশ রিটার্ন করা
        return match.group()
    return None

# প্রতিটি মেসেজ প্রসেস করে আউটপুট প্রিন্ট করা
for message in messages.strip().split('\n'):
    result = process_message(message)
    if result:
        print(result)