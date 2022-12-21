#![allow(dead_code)]
use lazy_static::lazy_static;
use regex::Regex;
use std::io;

#[derive(Debug)]
struct BluePrint {
    num: isize,
    costs: [[isize; 4]; 4],
    max_seen: isize,
    maxs: [isize; 4],
}

impl BluePrint {
    fn find_max(&mut self, time: isize) -> isize {
        let mut bots = [1, 0, 0, 0];
        let mut materials = [0, 0, 0, 0];
        self.find_max_int(&mut bots, &mut materials, time);
        self.max_seen
    }

    fn find_max_int(&mut self, bots: &mut [isize; 4], materials: &mut [isize; 4], time: isize) {
        if self.max_seen >= materials[3] + time * bots[3] + (time - 2) * (time - 1) / 2 {
            return;
        }
        if time == 0 {
            if self.max_seen < materials[3] {
                self.max_seen = materials[3];
            }
            return;
        }
        for i in 0..4 {
            materials[i] += bots[i];
        }
        for i in (0..4).rev() {
            if bots[i] >= self.maxs[i] {
                continue;
            }
            if self.costs[i]
                .iter()
                .zip(materials.iter())
                .all(|(a, b)| a <= b)
            {
                for j in 0..4 {
                    materials[j] -= self.costs[i][j];
                }
                bots[i] += 1;
                materials[i] -= 1;
                self.find_max_int(bots, materials, time - 1);
                materials[i] += 1;
                bots[i] -= 1;
                for j in 0..4 {
                    materials[j] += self.costs[i][j];
                }
            }
        }
        self.find_max_int(bots, materials, time - 1);
        for i in 0..4 {
            materials[i] -= bots[i];
        }
    }
}

fn get_bps() -> Vec<BluePrint> {
    lazy_static! {
        static ref RE: Regex = Regex::new(r"\d+").unwrap();
    }
    let mut rv = Vec::new();
    for line in io::stdin().lines() {
        let line = line.unwrap();
        let nums = RE
            .find_iter(&line)
            .filter_map(|digits| digits.as_str().parse().ok())
            .collect::<Vec<isize>>();
        let mut bp = BluePrint {
            num: nums[0],
            costs: [
                [nums[1], 0, 0, 0],
                [nums[2], 0, 0, 0],
                [nums[3], nums[4], 0, 0],
                [nums[5], 0, nums[6], 0],
            ],
            max_seen: 0,
            maxs: [0, 0, 0, 100],
        };
        for i in 0..3 {
            for j in 0..4 {
                if bp.maxs[i] < bp.costs[j][i] {
                    bp.maxs[i] = bp.costs[j][i];
                }
            }
        }
        rv.push(bp);
    }
    rv
}

fn main() {
    let mut bps = get_bps();
    let mut s = 0;
    for bp in bps.iter_mut() {
        s += bp.find_max(24) * bp.num;
    }
    println!("Part 1: {s}\n");
    s = 1;
    for bp in bps.iter_mut().take(3) {
        let b = bp.find_max(32);
        s *= b;
    }
    println!("Part 2: {s}");
}
