const fs = require('fs');
const path = require('path');

// 读取sanctuary.html文件
const filePath = path.join(__dirname, 'templates', 'sanctuary.html');
const content = fs.readFileSync(filePath, 'utf8');

// 提取JavaScript代码
const scriptMatches = content.match(/<script[^>]*>([\s\S]*?)<\/script>/gi);

if (scriptMatches) {
    scriptMatches.forEach((script, index) => {
        // 移除script标签，只保留JavaScript代码
        const jsCode = script.replace(/<script[^>]*>|<\/script>/gi, '');
        
        try {
            // 尝试解析JavaScript代码
            new Function(jsCode);
            console.log(`Script ${index + 1}: 语法正确`);
        } catch (error) {
            console.log(`Script ${index + 1}: 语法错误`);
            console.log(`错误信息: ${error.message}`);
            
            // 尝试找到错误位置
            const lines = jsCode.split('\n');
            if (error.message.includes('line')) {
                const lineMatch = error.message.match(/line (\d+)/);
                if (lineMatch) {
                    const lineNum = parseInt(lineMatch[1]);
                    console.log(`错误行: ${lines[lineNum - 1]}`);
                }
            }
        }
    });
} else {
    console.log('未找到JavaScript代码');
}