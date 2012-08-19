; File: 1.clj
; Description: http://projecteuler.net/problem=1

(print (apply + (filter (fn [x] (or (= 0 (mod x 5)) (= 0 (mod x 3)))) (range 3 1000))))
