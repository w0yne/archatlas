export function navFor(lang) {
 const zh = lang === 'zh', p = zh ? '/zh' : '';
 return [
  {text: zh ? '选择视图' : 'Choose a view', link:p+'/choose'},
  {text: zh ? '图型目录' : 'Catalogue', link:p+'/types/'},
  {text: zh ? '使用' : 'Use the skill', link:p+'/use/'},
  {text: zh ? '改进' : 'Improve', link:p+'/improve/'},
  {text: zh ? '术语与概念' : 'Glossary', link:zh ? '/zh/use/glossary' : '/glossary'},
  {text: zh ? '关于与许可' : 'About & licences', link:p+'/about'}
 ];
}
export function sidebarFor(lang, typeGroups) {
 const zh = lang === 'zh', p = zh ? '/zh' : '';
 return [
  {text:zh?'开始':'Start here',items:[...navFor(lang).filter(item=>!item.link.endsWith('/use/')&&!item.link.endsWith('/improve/')), ...(zh?[{text:'中英术语对照表',link:'/zh/glossary'}]:[])]},
  ...typeGroups,
  {text:zh?'使用 skill':'Use the skill',items:[
   {text:zh?'安装与首次运行':'Install and first run',link:p+'/use/'},
   {text:zh?'自主或引导模式':'Autonomous or guided',link:p+'/use/modes'},
   {text:zh?'从源码到架构图':'From code to diagrams',link:p+'/use/code-to-diagram'},
   {text:zh?'命令与限制':'Commands and limits',link:p+'/use/formats'}]},
  {text:zh?'改进':'Improve',items:[{text:zh?'贡献':'Contribute',link:p+'/improve/'},{text:zh?'评估改动':'Evaluate changes',link:p+'/improve/evals'}]}
 ];
}
