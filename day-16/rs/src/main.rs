use std::collections::HashMap;

#[derive(Clone, Debug)]
struct Valve {
    name: &'static str,
    rate: usize,
    connections: Vec<&'static str>,
    is_open: bool,
    num: usize,
}

fn init() -> HashMap<&'static str, Valve> {
    let mut hm = HashMap::new();
    let mut i = 0;
    let a = Valve {
        name: "AW",
        rate: 0,
        connections: vec!["DS", "AA"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "NT",
        rate: 4,
        connections: vec!["AO", "IT", "AM", "VZ"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "FI",
        rate: 0,
        connections: vec!["NK", "RH"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "NK",
        rate: 13,
        connections: vec!["VZ", "QE", "FI"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "ZB",
        rate: 0,
        connections: vec!["IC", "TX"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "DS",
        rate: 3,
        connections: vec!["ME", "JY", "OV", "RA", "AW"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "JT",
        rate: 0,
        connections: vec!["RA", "OE"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "OH",
        rate: 0,
        connections: vec!["KT", "AK"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "OE",
        rate: 9,
        connections: vec!["SH", "MR", "JT", "QI"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "CT",
        rate: 0,
        connections: vec!["JH", "NA"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "CB",
        rate: 0,
        connections: vec!["XC", "JH"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "EK",
        rate: 0,
        connections: vec!["GB", "ZZ"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "NA",
        rate: 0,
        connections: vec!["GL", "CT"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "JY",
        rate: 0,
        connections: vec!["DS", "IH"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "RA",
        rate: 0,
        connections: vec!["JT", "DS"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "QT",
        rate: 0,
        connections: vec!["ZG", "KM"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "SM",
        rate: 0,
        connections: vec!["AK", "AM"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "XC",
        rate: 11,
        connections: vec!["CB"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "BF",
        rate: 10,
        connections: vec!["BU", "MR"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "OV",
        rate: 0,
        connections: vec!["BV", "DS"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "GB",
        rate: 25,
        connections: vec!["EK"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "SD",
        rate: 0,
        connections: vec!["JF", "CN"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "IH",
        rate: 0,
        connections: vec!["JY", "KM"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "DF",
        rate: 0,
        connections: vec!["ON", "IC"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "BV",
        rate: 6,
        connections: vec!["OV", "JN", "ZG", "UF"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "PO",
        rate: 0,
        connections: vec!["AK", "QE"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "JH",
        rate: 12,
        connections: vec!["CB", "MI", "CT"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "CN",
        rate: 22,
        connections: vec!["SD"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "JF",
        rate: 0,
        connections: vec!["KM", "SD"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "QI",
        rate: 0,
        connections: vec!["MI", "OE"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "JN",
        rate: 0,
        connections: vec!["BV", "BS"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "TX",
        rate: 0,
        connections: vec!["KM", "ZB"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "ME",
        rate: 0,
        connections: vec!["VG", "DS"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "ON",
        rate: 0,
        connections: vec!["DF", "AA"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "GL",
        rate: 20,
        connections: vec!["NA"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "AA",
        rate: 0,
        connections: vec!["ON", "UF", "WR", "ML", "AW"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "BS",
        rate: 0,
        connections: vec!["JN", "IC"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "RH",
        rate: 0,
        connections: vec!["FI", "KT"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "BU",
        rate: 0,
        connections: vec!["BF", "BG"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "IT",
        rate: 0,
        connections: vec!["NT", "KT"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "MR",
        rate: 0,
        connections: vec!["OE", "BF"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "AO",
        rate: 0,
        connections: vec!["ML", "NT"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "KM",
        rate: 16,
        connections: vec!["WR", "IH", "QT", "TX", "JF"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "ML",
        rate: 0,
        connections: vec!["AO", "AA"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "VG",
        rate: 0,
        connections: vec!["ME", "IC"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "MI",
        rate: 0,
        connections: vec!["QI", "JH"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "AM",
        rate: 0,
        connections: vec!["NT", "SM"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "KT",
        rate: 23,
        connections: vec!["BG", "OH", "RH", "SH", "IT"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "AK",
        rate: 14,
        connections: vec!["SM", "PO", "OH"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "BG",
        rate: 0,
        connections: vec!["KT", "BU"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "QE",
        rate: 0,
        connections: vec!["NK", "PO"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "IC",
        rate: 17,
        connections: vec!["VG", "ZZ", "BS", "ZB", "DF"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "UF",
        rate: 0,
        connections: vec!["BV", "AA"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "SH",
        rate: 0,
        connections: vec!["KT", "OE"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "WR",
        rate: 0,
        connections: vec!["AA", "KM"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "ZZ",
        rate: 0,
        connections: vec!["IC", "EK"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "ZG",
        rate: 0,
        connections: vec!["BV", "QT"],
        is_open: false,
        num: i,
    };
    i += 1;
    hm.insert(a.name, a);
    let a = Valve {
        name: "VZ",
        rate: 0,
        connections: vec!["NK", "NT"],
        is_open: false,
        num: i,
    };
    hm.insert(a.name, a);
    hm
}

fn search(
    nodes: &mut HashMap<&'static str, Valve>,
    key: &'static str,
    potential: usize,
    total: usize,
    mut remaining: isize,
    mut max_seen: usize,
    open: usize,
    //                   open   remaining, where
    cache: &mut HashMap<(usize, isize, &'static str), (usize, usize)>,
) -> (usize, usize) {
    let mut max_mask = 0;
    if let Some(v) = cache.get(&(open, remaining, key)) {
        return *v;
    }
    if total + potential * (remaining as usize) < max_seen {
        return (0, 0xffffffffff);
    }
    if remaining <= 0 {
        if total > max_seen {
            println!("{total}");
            return (total, open);
        }
        return (0, 0xffffffffff);
    }
    let node = nodes.get_mut(key).unwrap().clone();
    if !node.is_open && node.rate != 0 {
        nodes.get_mut(key).unwrap().is_open = true;
        remaining -= 1;
        let new_tot = total + node.rate * (remaining as usize);
        for nn in node.connections.iter() {
            let s = search(
                nodes,
                nn,
                potential - node.rate,
                new_tot,
                remaining - 1,
                max_seen,
                open | (1 << node.num),
                cache,
            );
            if s.0 > max_seen {
                max_seen = s.0;
                max_mask = s.1;
            }
        }
        remaining += 1;
        nodes.get_mut(key).unwrap().is_open = false;
    }
    for nn in node.connections.iter() {
        let s = search(
            nodes,
            nn,
            potential - node.rate,
            total,
            remaining - 1,
            max_seen,
            open,
            cache,
        );
        if s.0 > max_seen {
            max_seen = s.0;
            max_mask = s.1;
        }
    }
    cache.insert((open, remaining, key), (max_seen, open));
    (max_seen, max_mask)
}

fn main() {
    let mut nodes = init();
    let potential = nodes.values().map(|n| n.rate).sum();
    let (max_flow, mask) = search(
        &mut nodes,
        "AA",
        potential,
        0,
        26,
        0,
        0,
        &mut HashMap::new(),
    );
    for node in nodes.values_mut() {
        if (mask & 1 << node.num) != 0 {
            node.rate = 0;
        }
    }
    let potential = nodes.values().map(|n| n.rate).sum();
    let (max_flow1, _) = search(
        &mut nodes,
        "AA",
        potential,
        0,
        26,
        0,
        0,
        &mut HashMap::new(),
    );
    println!("{}", max_flow1 + max_flow);
}
