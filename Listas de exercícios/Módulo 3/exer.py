
# def merge(a,b):
#     c = []
#     while len(a) != 0 and len(b) != 0:
#         if a[0] < b[0]:
#             c.append(a[0])
#             a.remove(a[0])
#         else:
#             c.append(b[0])
#             b.remove(b[0])
#     if len(a) == 0:
#         c += b
#     else:
#         c += a
#     return c


# https://leetcode.com/problems/median-of-two-sorted-arrays/

def encontrar_mediana(nums1: list[int], nums2: list[int]) -> float:
    ref_nums1=0
    ref_nums2=0
    ref_nums3=0
    nums3 = sorted(nums1 + nums2)  
    while ref_nums1 < len(nums1) and ref_nums2 < len(nums2):
        if nums1[ref_nums1] < nums2[ref_nums2]:
            nums3[ref_nums3] = nums1[ref_nums1]
            ref_nums1 = ref_nums1 + 1
        else:
            nums3[ref_nums3]=nums2[ref_nums2]
            ref_nums2 = ref_nums2 + 1
            ref_nums3 = ref_nums3 + 1

        while ref_nums1 < len(nums1):
            nums3[ref_nums3]=nums1[ref_nums1]
            ref_nums1=ref_nums1+1
            ref_nums3=ref_nums3+1

        while ref_nums2 < len(nums2):
            nums3[ref_nums3]=nums2[ref_nums2]
            ref_nums2=ref_nums2+1
            ref_nums3=ref_nums3+1