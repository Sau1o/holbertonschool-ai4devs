class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        # parse Apache log line (assumes standard format where status is at index 8)
        parts = line.split()
        if len(parts) < 9:
            return {"status": 0}
        return {"status": int(parts[8])}

    def analyze(self, lines: list) -> dict:
        total = len(lines)
        if total == 0:
            return {"total_requests": 0, "error_rate": 0.0}
            
        errors = sum(1 for l in lines if self.parse_line(l)["status"] >= 400)
        return {"total_requests": total, "error_rate": (errors / total) * 100}
