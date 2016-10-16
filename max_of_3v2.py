# Программа, которая получает на вход три целых числа, по одному числу в строке,
# и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
nums1=int(input())
nums2=int(input())
nums3=int(input())

if nums1>=nums2>=nums3:
    top=nums1
    mid=nums2
    bot=nums3
elif nums1>=nums3>=nums2:
    top=nums1
    mid=nums3
    bot=nums2
elif nums2>=nums1>=nums3:
    top=nums2
    mid=nums1
    bot=nums3
elif nums2>=nums3>=nums1:
    top=nums2
    mid=nums3
    bot=nums1
elif nums3>=nums1>=nums2:
    top=nums3
    mid=nums1
    bot=nums2
elif nums3>=nums2>=nums1:
    top=nums3
    mid=nums2
    bot=nums1

print(top,'\n',bot,'\n',mid)
