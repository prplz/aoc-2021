const std = @import("std");

pub fn readNumbers(comptime T: type, allocator: *std.mem.Allocator, path: []const u8) ![]T {
    const contents = try std.fs.cwd().readFileAlloc(allocator, path, std.math.maxInt(usize));
    defer allocator.free(contents);
    var nums = std.ArrayList(T).init(allocator);
    defer nums.deinit();
    var iter = std.mem.split(u8, contents, "\n");
    while (iter.next()) |line| {
        if (line.len > 0) {
            const num = try std.fmt.parseInt(T, line, 10);
            try nums.append(num);
        }
    }
    return nums.toOwnedSlice();
}
