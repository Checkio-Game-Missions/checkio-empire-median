TESTS = {
    "Level_1": [
        {"input": [1, 2, 3, 4, 5], "answer": 3, "explanation": True},
        {"input": [3, 1, 2, 5, 3], "answer": 3, "explanation": True},
        {"input": [1, 300, 2, 200, 1], "answer": 2, "explanation": True},
        {"input": [3, 6, 20, 99, 10, 15], "answer": 12.5, "explanation": True},
        {
            "input": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            "answer": 5,
            "explanation": True
        },
        {
            "input": [0, 7, 1, 8, 4, 9, 5, 6, 2, 3],
            "answer": 4.5, "explanation": True
        },
        {"input": [33, 56, 62], "answer": 56, "explanation": True},
        {"input": [21, 56, 84, 82, 52, 9], "answer": 54, "explanation": True},
        {"input": [100, 1, 1, 1, 1, 1, 1], "answer": 1, "explanation": True},
        {"input": [64, 6, 92, 7, 70, 5], "answer": 35.5, "explanation": True},
        {
            "input": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "answer": 1
        },
        {
            "input": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            "answer": 2
        },

        {
            "input": [999999, 1],
            "answer": 500000
        },
        {
            "input": [999999, 1, 999999],
            "answer": 999999
        },

        {
            "input": [0, 1],
            "answer": 0.5,
            "explanation": True
        },

        {
            "input": [100000, 999999, 199999, 200000, 200000],
            "answer": 200000
        },

        {
            "input": [890, 687, 847, 627, 942, 395, 752, 736, 45, 337, 203, 569, 590, 750, 484, 691, 789, 676, 99, 204,
                      543, 573, 782, 814, 935, 917, 857, 388, 843, 621, 190, 222, 71, 378, 744, 114, 673, 328, 968, 930,
                      938, 656, 236, 47, 259, 639, 887, 952, 972, 619, 434, 835, 273, 191, 961, 563, 200, 988, 616, 919,
                      837, 899, 905, 481, 133, 159, 641, 229, 213, 983, 175, 999, 131, 944, 303, 714, 243, 212, 810,
                      491, 826, 176, 778, 599, 525, 343, 982, 967, 281, 500, 722, 613, 896, 402, 683, 532, 925, 666,
                      801, 651, 277, 571, 740, 393, 453, 620, 74, 134, 348, 61, 854, 28, 675, 423, 703, 741, 363, 698,
                      585, 654, 382, 321, 692, 432, 499, 870, 904, 562, 410, 209, 678, 166, 428, 349, 251, 256, 907,
                      333, 39, 368, 825, 280, 299, 143, 670, 512, 520, 247, 180, 302, 959, 87, 634, 886, 922, 381, 530,
                      135, 301, 551, 863, 278, 524, 305, 998, 685, 943, 502, 112, 121, 124, 596, 33, 841, 34, 697, 338,
                      162, 710, 149, 316, 672, 885, 335, 800, 38, 93, 347, 756, 308, 518, 861, 459, 496, 404, 866, 522,
                      534, 769, 96, 923, 44, 831, 78, 72, 913, 540, 809, 58, 448, 359, 220, 669, 12, 49, 606, 413, 298,
                      438, 751, 745, 986, 4, 796, 728, 279, 902, 912, 862, 457, 290, 878, 602, 882, 123, 476, 411, 559,
                      218, 70, 648, 260, 624, 82, 962, 992, 545, 390, 664, 804, 122, 73, 276, 742, 350, 245, 844, 817,
                      640, 417, 18, 465, 201, 125, 638, 806, 785, 172, 62, 132, 389, 903, 597, 13, 556, 467, 853, 40,
                      600, 652, 195, 230, 146, 860, 734, 614, 392, 43, 865, 20, 850, 479, 811, 296, 231, 463, 329, 161,
                      876, 3, 490, 436, 375, 383, 424, 749, 958, 456, 35, 406, 446, 792, 91, 880, 921, 757, 991, 232,
                      558, 832, 766, 928, 929, 272, 647, 973, 830, 426, 207, 926, 318, 934, 618, 164, 422, 733, 52, 515,
                      360, 977, 598, 325, 765, 851, 306, 421, 217, 893, 840, 265, 274, 527, 583, 816, 288, 570, 81, 327,
                      786, 918, 601, 681, 762, 188, 505, 128, 126, 361, 536, 845, 54, 30, 472, 910, 984, 471, 572, 667,
                      538, 285, 130, 568, 731, 397, 427, 767, 812, 119, 431, 405, 205, 931, 116, 357, 493, 31, 129, 579,
                      548, 948, 578, 686, 51, 241, 637, 909, 547, 371, 289, 186, 794, 529, 746, 971, 264, 234, 960, 849,
                      695, 873, 157, 591, 339, 141, 503, 592, 979, 100, 761, 271, 37, 473, 295, 106, 189, 969, 753, 577,
                      489, 452, 95, 631, 312, 966, 261, 310, 255, 994, 635, 8, 889, 770, 799, 868, 97, 821, 867, 526,
                      589, 649, 92, 848, 151, 332, 906, 419, 706, 169, 469, 793, 109, 447, 104, 911, 760, 154, 594, 997,
                      480, 477, 341, 511, 805, 985, 747, 103, 57, 461, 163, 713, 352, 813, 262, 105, 291, 366, 611, 370,
                      300, 802, 575, 739, 177, 815, 888, 440, 679, 700, 939, 144, 776, 877, 53, 528, 441, 501, 224, 282,
                      650, 693, 173, 541, 293, 901, 77, 719, 396, 445, 564, 535, 531, 344, 970, 454, 237, 894, 179, 408,
                      622, 946, 387, 474, 951, 561, 455, 286, 937, 206, 478, 401, 945, 199, 86, 712, 29, 574, 10, 950,
                      358, 185, 978, 864, 127, 32, 696, 775, 342, 964, 509, 822, 65, 897, 304, 284, 791, 235, 178, 250,
                      550, 488, 369, 836, 748, 160, 542, 855, 420, 14, 875, 779, 372, 101, 27, 340, 715, 102, 924, 449,
                      818, 646, 824, 820, 711, 494, 730, 313, 883, 219, 916, 168, 108, 633, 498, 674, 842, 26, 702, 425,
                      699, 111, 228, 36, 546, 724, 764, 156, 645, 632, 828, 663, 439, 608, 60, 435, 364, 226, 593, 797,
                      603, 244, 345, 16, 356, 216, 900, 643, 183, 194, 415, 725, 798, 788, 48, 307, 940, 689, 965, 418,
                      989, 684, 433, 379, 268, 17, 690, 117, 587, 852, 89, 198, 174, 238, 957, 283, 773, 662, 588, 196,
                      513, 466, 560, 625, 64, 153, 323, 819, 80, 954, 963, 83, 5, 787, 248, 320, 451, 85, 275, 891, 580,
                      98, 914, 403, 519, 514, 554, 726, 738, 708, 617, 19, 56, 709, 553, 604, 202, 665, 252, 193, 655,
                      790, 324, 615, 497, 993, 949, 346, 380, 464, 267, 386, 609, 987, 90, 727, 110, 908, 555, 996, 657,
                      659, 79, 884, 936, 309, 636, 41, 460, 1, 595, 626, 55, 416, 75, 716, 145, 294, 374, 140, 158, 933,
                      504, 399, 605, 351, 107, 287, 833, 623, 263, 718, 758, 257, 717, 754, 315, 735, 507, 995, 214, 2,
                      377, 920, 84, 67, 808, 326, 22, 412, 508, 628, 314, 227, 249, 780, 0, 834, 975, 9, 147, 549, 872,
                      610, 892, 947, 781, 858, 566, 139, 557, 59, 955, 941, 586, 544, 932, 743, 25, 430, 729, 297, 197,
                      823, 171, 732, 120, 215, 155, 680, 394, 658, 6, 981, 400, 630, 334, 331, 362, 24, 482, 385, 856,
                      365, 353, 677, 330, 46, 707, 759, 165, 115, 768, 974, 552, 407, 723, 322, 42, 486, 458, 429, 803,
                      772, 246, 927, 506, 956, 523, 783, 210, 182, 319, 239, 629, 881, 76, 976, 721, 391, 533, 539, 661,
                      874, 409, 829, 763, 653, 682, 225, 233, 184, 612, 582, 565, 94, 895, 468, 258, 63, 694, 443, 137,
                      367, 607, 567, 398, 521, 720, 642, 148, 118, 774, 211, 113, 138, 990, 354, 668, 688, 807, 384, 66,
                      376, 192, 223, 69, 846, 859, 373, 784, 23, 487, 516, 755, 266, 470, 462, 980, 15, 88, 584, 517,
                      771, 21, 537, 7, 208, 485, 915, 336, 510, 11, 270, 414, 839, 50, 705, 871, 68, 221, 170, 317, 450,
                      181, 898, 254, 444, 437, 660, 827, 671, 355, 253, 187, 442, 495, 838, 136, 879, 576, 777, 644,
                      311, 483, 167, 240, 269, 704, 152, 475, 581, 492, 242, 150, 795, 701, 142, 953, 292, 869, 737],
            "answer": 499.5
        },
        {
            "input": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0],
            "answer": 0
        },
        {
            "input": [2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 2, 2,
                      2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 2, 2,
                      2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 1, 2, 0, 2, 0, 2, 0,
                      0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 0, 2, 2, 2,
                      2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0,
                      2, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2, 0,
                      2, 2, 0],
            "answer": 1
        },


        {"input": [64, 6, 92, 7, 70, 5], "answer": 35.5, "explanation": True},
    ]
}
