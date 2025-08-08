use std::collections::HashMap;

impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n > 5000 {
            return 1.0;
        }
        let units = ((n as f64) / 25.0).ceil() as i32;
        let mut cache: HashMap<(i32, i32), f64> = HashMap::new();

        fn calc_prob(a: i32, b: i32, memo: &mut HashMap<(i32, i32), f64>) -> f64 {
            if a <= 0 && b <= 0 {
                return 0.5;
            }
            if a <= 0 {
                return 1.0;
            }
            if b <= 0 {
                return 0.0;
            }
            if let Some(&v) = memo.get(&(a, b)) {
                return v;
            }
            let prob = 0.25 * (
                calc_prob(a - 4, b, memo) +
                calc_prob(a - 3, b - 1, memo) +
                calc_prob(a - 2, b - 2, memo) +
                calc_prob(a - 1, b - 3, memo)
            );
            memo.insert((a, b), prob);
            prob
        }

        calc_prob(units, units, &mut cache)
    }
}