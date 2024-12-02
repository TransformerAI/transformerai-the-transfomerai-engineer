from typing import List
class Solution:
    """
    Given two version strings, version1 and version2, compare them. 
    A version string consists of revisions separated by dots '.'. 
    The value of the revision is its integer conversion ignoring 
    leading zeros.

    To compare version strings, compare their revision values in 
    left-to-right order. If one of the version strings has fewer 
    revisions, treat the missing revision values as 0.

    Return the following:
        If version1 < version2, return -1.
        If version1 > version2, return 1.
        Otherwise, return 0.
    """
    def compareVersion(self, version1: str, version2: str) -> int:
        def get_version(version: str) -> List[int]:
            ver_components = version.split(".")
            version = []
            for ver_com in ver_components:
                version.append(int(ver_com))
            return version
        
        verarr_1 = get_version(version1)
        verarr_2 = get_version(version2)
        arrlen = max(len(verarr_1), len(verarr_2))
        if len(verarr_1) < len(verarr_2):
            for i in range(arrlen - len(verarr_1)):
                verarr_1.append(0)
        elif len(verarr_1) > len(verarr_2):
            for i in range(arrlen - len(verarr_2)):
                verarr_2.append(0)
        
        compare = [0] * arrlen
        for i in range(arrlen):
            if verarr_1[i] == verarr_2[i]:
                compare[i] = (0, arrlen - i)
            elif verarr_1[i] > verarr_2[i]:
                compare[i] = (1, arrlen - i)
            elif verarr_1[i] < verarr_2[i]:
                compare[i] = (-1, arrlen - i)

        for diff, boost in compare:
            if diff == 0:
                continue
            else:
                return diff
        return 0
        
if __name__ == "__main__":
    sol = Solution()
    version1 = "1.2"
    version2 = "1.10"
    output =  -1
    out = sol.compareVersion(version1, version2)
    print(out)
    version1 = "1.01"
    version2 = "1.001"
    output =  0
    out = sol.compareVersion(version1, version2)
    print(out)
    
    version1 = "1.0"
    version2 = "1.0.0.0"
    output =  0
    out = sol.compareVersion(version1, version2)
    print(out)
