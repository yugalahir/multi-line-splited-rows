# Multi-line-splited-rows

This script is usefull when your data splieted into mutilple rows and you want to merge in its parent row.
Example:-

Amount Total Sales
1 R8-O-C1
  -> Hollister-KSA-26Nov2019- 
  -> 4 DaySale Campaign Date: 28-Nov2019
  -> 3 days left: Hollister is on 40% off everything except perfumes!
  -> Visit us today. T&C apply.
  -> No. Of Recipients: 5175 Credits Require: 12,222.2725
  -> 0.055 0.00 0.00 672.27
2 R8-O-C1
  -> Hollister-KSA-11Nov2019 Campaign Date: 11Nov2019 Arabic
  -> Text
  -> No. Of Recipients: 5170 Credits Require: 36,651.8164
  -> 0.055 0.00 0.00 2,015.86
3 R8-O-C1
  -> Abercrombie-KSA-11Nov2019 Campaign Date: 11Nov2019
  -> Arabic Text
  -> No. Of Recipients: 2,875 Credits Require: 27,171
  -> 0.055 0.00 0.00 1,494.41
  
  And you wanted to merge the -> arrow rows to its main parent row then this script is use full
  after runnig this script you will get the following output-:
  
  1 R8-O-C1 Hollister-KSA-26Nov2019- 4 DaySale Campaign Date: 28-Nov2019 3 days left: Hollister is on 40% off everything except perfumes! Visit us today. T&C apply. No. Of Recipients:           5175 Credits Require: 12,222.2725 0.055 0.00 0.00 672.27
  
  2 R8-O-C1 Hollister-KSA-11Nov2019 Campaign Date: 11Nov2019 Arabic Text No. Of Recipients: 5170 Credits Require: 36,651.8164 0.055 0.00 0.00 2,015.86
  
  3 R8-O-C1 Abercrombie-KSA-11Nov2019 Campaign Date: 11Nov2019 Arabic Text No. Of Recipients: 2,875 Credits Require: 27,171 0.055 0.00 0.00 1,494.41
  
  Thank you
  
