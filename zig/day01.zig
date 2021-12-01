const std = @import("std");
const util = @import("util.zig");

test {
    const nums = try util.readNumbers(u32, std.testing.allocator, "../inputs/01.txt");
    defer std.testing.allocator.free(nums);

    var part1: usize = 0;
    var i: usize = 0;
    while (i < nums.len - 1) : (i += 1) {
        if (nums[i + 1] > nums[i]) {
            part1 += 1;
        }
    }
    try std.testing.expectEqual(@as(usize, 1557), part1);

    var part2: usize = 0;
    i = 0;
    while (i < nums.len - 3) : (i += 1) {
        if (nums[i + 3] > nums[i]) {
            part2 += 1;
        }
    }
    try std.testing.expectEqual(@as(usize, 1608), part2);
}
