module Main
where
import System.IO
import Data.List

main = print $ maximumBy (\a b -> compare (snd a) (snd b)) collatzip

collatzip = zip [10..1000000] (map length $ map collatz_chain [10..1000000])

collatz_chain :: Integer -> [Integer]
collatz_chain 1 = [1]
collatz_chain n | even n = n : (collatz_chain $ div n 2)
                | otherwise = n : (collatz_chain $ 3 * n + 1)
